from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from .models import *

import os
import json
import datetime
import requests
import itertools

def index(request):
    events = []

    event_hosts = EventHost.objects.all()

    access_token = json.loads(requests.get(
        "https://graph.facebook.com/oauth/access_token?client_id=" + os.environ.get('APP_ID') + "&client_secret=" + os.environ.get('APP_SECRET')  + "&grant_type=client_credentials").content.decode('utf-8'))['access_token']

    def get_host_events(host_ids):
        for event in event_hosts:
            result = json.loads(requests.get(
                "https://graph.facebook.com/" + str(event.host_id) + "/?fields=events{cover,name,attending_count,interested_count,start_time,end_time,place}&access_token=" + access_token).content.decode('utf-8'))['events']['data']
            events.append(result)

    get_host_events(events)

    events_popular = sorted(list(itertools.chain.from_iterable(events)), key=lambda k: k['attending_count'], reverse=True) 

    return render(request, 'index.html', {"events": events_popular, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200')})

def event_detail(request, event_id):

    def get_event(id):
        result = json.loads(requests.get(
            "https://graph.facebook.com/" + id + "/?fields=cover,name,description,attending_count,interested_count,start_time,end_time,place&access_token=" + access_token).content.decode('utf-8'))
        return result
        
    access_token = json.loads(requests.get(
        "https://graph.facebook.com/oauth/access_token?client_id=" + os.environ.get('APP_ID') + "&client_secret=" + os.environ.get('APP_SECRET')  + "&grant_type=client_credentials").content.decode('utf-8'))['access_token']
    
    event = get_event(event_id)

    try:
        event['name']
    except KeyError:
        raise Http404("event does not exist") 
        
    return render(request, 'event_detail.html', {'event': event})