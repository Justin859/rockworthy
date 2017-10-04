from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

from .models import *
from .forms import *

import os
import json
import datetime
import requests
import itertools
import urllib.request
import urllib.parse

def get_access_token():
    access_token = json.loads(requests.get(
        "https://graph.facebook.com/oauth/access_token?client_id=" + os.environ.get('APP_ID') + "&client_secret=" + os.environ.get('APP_SECRET')  + "&grant_type=client_credentials").content.decode('utf-8'))['access_token']
    return access_token

def get_events_particular(event_type, host_type):
    batch_values = []
    events = []
    event_hosts = EventHost.objects.filter(event_type__in=event_type, host_type__in=host_type)

    for host in event_hosts:
        batch_values.append({"method": "GET", "relative_url": host.host_id + "/?fields=events{cover,name,attending_count,ticket_uri,interested_count,start_time,end_time,place}"})

    url = "https://graph.facebook.com"
    access_token = get_access_token()

    values = {"access_token":access_token, "batch":batch_values, "include_headers": "false"}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.readall().decode('utf-8')
    result = json.loads(respData)

    for event in result:
        events.append(json.loads(event['body'])['events']['data'])

    events = list(itertools.chain.from_iterable(events))    


    return events

def index(request):

    events = get_events_particular(['Live Shows', 'Art Exhibition', 'Craft Market'], ['Venue', 'Special Event'])

    return render(request, 'index.html', {"events": events})

def event_detail(request, event_id):

    access_token = get_access_token()

    event = json.loads(requests.get(
        "https://graph.facebook.com/" + event_id + "/?fields=cover,name,ticket_uri,description,attending_count,interested_count,start_time,end_time,place&access_token=" + access_token).content.decode('utf-8'))
        
    try:
        event['name']
    except KeyError:
        raise Http404("event does not exist on Rock Worthy") 
        
    return render(request, 'Events/event_detail.html', {'event': event})


def venues(request):
    hosts = []
    access_token = get_access_token()

    event_hosts = EventHost.objects.filter(host_type='Venue')

    for event in event_hosts:
        result = json.loads(requests.get(
            "https://graph.facebook.com/" + str(event.host_id) + "/?fields=fan_count,picture,category,name&access_token=" + access_token).content.decode('utf-8'))
        hosts.append(result)       
    
    hosts = sorted(hosts, key=lambda k: k['fan_count'], reverse=True) 

    return render(request, 'Venues/venues.html', {"hosts": hosts})


def venue_detail(request, venue_id):

    event_host = EventHost.objects.filter(host_id=venue_id)[0]

    access_token = get_access_token()

    venue = json.loads(requests.get(
        "https://graph.facebook.com/" + venue_id + "/?fields=cover,events{cover,ticket_uri,name,place,attending_count,interested_count,start_time,end_time},fan_count,picture,category,name&access_token=" + access_token).content.decode('utf-8'))

    try:
        venue['id']
    except KeyError:
        raise Http404("Venue does not exists on Rock Worthy")

    return render(request, 'Venues/venue_detail.html', {"venue": venue, "event_host": event_host})

def live_music(request):

    events = get_events_particular(['Live Shows'], ['Venue', 'Special Event'])

    return render(request, 'Events/livemusic.html', {"events": events})

def art_exhibition(request):

    events = get_events_particular(['Art Exhibition'], ['Venue'])

    return render(request, 'Events/artexhibitions.html', {"events": events})

def craft_market(request):

    events = get_events_particular(['Craft Market'], ['Venue'])

    return render(request, 'Events/craftmarkets.html', {"events": events})

def special_events(request):

    events = get_events_particular(['Live Shows'], ['Special Event'])

    return render(request, 'Events/special_events.html', {"events": events})


def contact(request):
    if request.method == 'POST':
        form = Query(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            query = form.cleaned_data['query']

            try:
                send_mail('rockworthy.co.za Query', 'email: ' + email + '\n\nclient name: ' + name + '\n\nclient query: \n\n' + query, 'query@rockworthy.co.za', ['info@rockworthy.co.za'])
            except BadHeaderError:
                return HttpResponse('Invalid Header found.')

            messages.success(request, 'Your query has been sent. We will contact you as soon as possible.')
            return HttpResponseRedirect('/contact/') 
    else:
        form = Query()
    return render(request, 'contact.html', {'form': form})

def about(request):

    return render(request, 'about.html')

