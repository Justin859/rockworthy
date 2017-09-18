from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from .models import *

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

    event_hosts = EventHost.objects.all()

    access_token = get_access_token()

    for event in event_hosts:
        result = json.loads(requests.get(
            "https://graph.facebook.com/" + str(event.host_id) + "/?fields=events{cover,name,attending_count,interested_count,start_time,end_time,place}&access_token=" + access_token).content.decode('utf-8'))['events']['data']
        events.append(result)

    events_popular = list(itertools.chain.from_iterable(events))

    return render(request, 'index.html', {"events": events_popular, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200')})

def event_detail(request, event_id):

    access_token = get_access_token()

    event = json.loads(requests.get(
        "https://graph.facebook.com/" + event_id + "/?fields=cover,name,description,attending_count,interested_count,start_time,end_time,place&access_token=" + access_token).content.decode('utf-8'))
        
    try:
        event['name']
    except KeyError:
        raise Http404("event does not exist on Rock Worthy") 
        
    return render(request, 'event_detail.html', {'event': event})


def venues(request):
    hosts = []
    access_token = get_access_token()

    event_hosts = EventHost.objects.filter(host_type='Venue')

    for event in event_hosts:
        result = json.loads(requests.get(
            "https://graph.facebook.com/" + str(event.host_id) + "/?fields=fan_count,picture,category,name&access_token=" + access_token).content.decode('utf-8'))
        hosts.append(result)       
    
    hosts = sorted(hosts, key=lambda k: k['fan_count'], reverse=True) 

    return render(request, 'venues.html', {"hosts": hosts})


def venue_detail(request, venue_id):

    access_token = get_access_token()

    venue = json.loads(requests.get(
        "https://graph.facebook.com/" + venue_id + "/?fields=cover,events{cover,name,attending_count,interested_count,start_time,end_time},fan_count,picture,category,name&access_token=" + access_token).content.decode('utf-8'))

    try:
        venue['id']
    except KeyError:
        raise Http404("Venue does not exists on Rock Worthy")

    return render(request, 'venue_detail.html', {"venue": venue, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200')})

def live_music(request):
    events = []

    event_hosts = EventHost.objects.filter(event_type='Live Shows')

    access_token = get_access_token()

    for event in event_hosts:
        result = json.loads(requests.get(
            "https://graph.facebook.com/" + str(event.host_id) + "/?fields=events{cover,name,attending_count,interested_count,start_time,end_time,place}&access_token=" + access_token).content.decode('utf-8'))['events']['data']
        events.append(result)

    events_popular = list(itertools.chain.from_iterable(events))

    return render(request, 'livemusic.html', {"events": events_popular, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200')})

def art_exhibition(request):
    events = []

    event_hosts = EventHost.objects.filter(event_type='Art Exhibition')

    access_token = get_access_token()

    for event in event_hosts:
        result = json.loads(requests.get(
            "https://graph.facebook.com/" + str(event.host_id) + "/?fields=events{cover,name,attending_count,interested_count,start_time,end_time,place}&access_token=" + access_token).content.decode('utf-8'))['events']['data']
        events.append(result)

    events_popular = list(itertools.chain.from_iterable(events))

    return render(request, 'artexhibitions.html', {"events": events_popular, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200')})

def craft_market(request):
    events = []

    event_hosts = EventHost.objects.filter(event_type='Craft Market')

    access_token = get_access_token()

    for event in event_hosts:
        result = json.loads(requests.get(
            "https://graph.facebook.com/" + str(event.host_id) + "/?fields=events{cover,name,attending_count,interested_count,start_time,end_time,place}&access_token=" + access_token).content.decode('utf-8'))['events']['data']
        events.append(result)

    events_popular = list(itertools.chain.from_iterable(events))

    return render(request, 'craftmarkets.html', {"events": events_popular, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200')})    