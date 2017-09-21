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


def get_access_token():
    access_token = json.loads(requests.get(
        "https://graph.facebook.com/oauth/access_token?client_id=" + os.environ.get('APP_ID') + "&client_secret=" + os.environ.get('APP_SECRET')  + "&grant_type=client_credentials").content.decode('utf-8'))['access_token']
    return access_token

def index(request):
    events = []
    date_today = datetime.date.today()
    week_day = date_today.weekday()

    if (week_day == 0 or week_day == 1 or week_day == 2 or week_day == 3):
        weekend_start = date_today + datetime.timedelta(days=4-week_day)
        weekend_stop = weekend_start + datetime.timedelta(days=2)
        mid_weekend = weekend_start + datetime.timedelta(days=1)
    else:
        weekend_start = date_today
        weekend_stop = weekend_start + datetime.timedelta(days=6-week_day)
        mid_weekend = weekend_start + datetime.timedelta(days=1)

    event_hosts = EventHost.objects.all()

    access_token = get_access_token()

    for event in event_hosts:
        result = json.loads(requests.get(
            "https://graph.facebook.com/" + event.host_id + "/?fields=events{cover,name,attending_count,interested_count,start_time,end_time,place}&access_token=" + access_token).content.decode('utf-8'))['events']['data']
        events.append(result)

    events_popular = list(itertools.chain.from_iterable(events))

    return render(request, 'index.html', {"events": events_popular, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200'), "weekend_start": weekend_start, "weekend_stop": weekend_stop, "mid_weekend": mid_weekend, "date_today": date_today})

def event_detail(request, event_id):

    access_token = get_access_token()

    event = json.loads(requests.get(
        "https://graph.facebook.com/" + event_id + "/?fields=cover,name,description,attending_count,interested_count,start_time,end_time,place&access_token=" + access_token).content.decode('utf-8'))
        
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
        "https://graph.facebook.com/" + venue_id + "/?fields=cover,events{cover,name,attending_count,interested_count,start_time,end_time},fan_count,picture,category,name&access_token=" + access_token).content.decode('utf-8'))

    try:
        venue['id']
    except KeyError:
        raise Http404("Venue does not exists on Rock Worthy")

    return render(request, 'Venues/venue_detail.html', {"venue": venue, "event_host": event_host, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200')})

def live_music(request):
    events = []
    date_today = datetime.date.today()
    week_day = date_today.weekday()

    if (week_day == 0 or week_day == 1 or week_day == 2 or week_day == 3):
        weekend_start = date_today + datetime.timedelta(days=4-week_day)
        weekend_stop = weekend_start + datetime.timedelta(days=2)
        mid_weekend = weekend_start + datetime.timedelta(days=1)
    else:
        weekend_start = date_today
        weekend_stop = weekend_start + datetime.timedelta(days=6-week_day)
        mid_weekend = weekend_start + datetime.timedelta(days=1)

    event_hosts = EventHost.objects.filter(event_type='Live Shows')

    access_token = get_access_token()

    for event in event_hosts:
        result = json.loads(requests.get(
            "https://graph.facebook.com/" + str(event.host_id) + "/?fields=events{cover,name,attending_count,interested_count,start_time,end_time,place}&access_token=" + access_token).content.decode('utf-8'))['events']['data']
        events.append(result)

    events_popular = list(itertools.chain.from_iterable(events))

    return render(request, 'Events/livemusic.html', {"events": events_popular, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200'), "weekend_start": weekend_start, "weekend_stop": weekend_stop, "mid_weekend": mid_weekend, "date_today": date_today})

def art_exhibition(request):
    events = []

    event_hosts = EventHost.objects.filter(event_type='Art Exhibition')

    access_token = get_access_token()

    for event in event_hosts:
        result = json.loads(requests.get(
            "https://graph.facebook.com/" + str(event.host_id) + "/?fields=events{cover,name,attending_count,interested_count,start_time,end_time,place}&access_token=" + access_token).content.decode('utf-8'))['events']['data']
        events.append(result)

    events_popular = list(itertools.chain.from_iterable(events))

    return render(request, 'Events/artexhibitions.html', {"events": events_popular, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200')})

def craft_market(request):
    events = []

    event_hosts = EventHost.objects.filter(event_type='Craft Market')

    access_token = get_access_token()

    for event in event_hosts:
        result = json.loads(requests.get(
            "https://graph.facebook.com/" + str(event.host_id) + "/?fields=events{cover,name,attending_count,interested_count,start_time,end_time,place}&access_token=" + access_token).content.decode('utf-8'))['events']['data']
        events.append(result)

    events_popular = list(itertools.chain.from_iterable(events))

    return render(request, 'Events/craftmarkets.html', {"events": events_popular, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200')})

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

            messages.success(request, 'Thank you for your query! Your query has been sent. We will contact you as soon as possible.')
            return HttpResponseRedirect('/contact/') 
    else:
        form = Query()
    return render(request, 'contact.html', {'form': form})

def about(request):

    return render(request, 'about.html')   