from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
                "https://graph.facebook.com/" + str(event.host_id) + "/?fields=events{cover,name,attending_count,start_time,place}&access_token=" + access_token).content.decode('utf-8'))['events']['data']
            events.append(result)

    get_host_events(events)
    events = list(itertools.chain.from_iterable(events))
    events_popular = sorted(events, key=lambda k: k['attending_count'], reverse=True) 

    return render(request, 'index.html', {"events": events_popular, "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200')})