"""rockworthy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rockworthy import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^event/(?P<event_id>[0-9]+)/detail/$', views.event_detail, name='event_detail'),
    url(r'^venues/$', views.venues, name='venues'),
    url(r'^venue/(?P<venue_id>[0-9]+)/$', views.venue_detail, name='venue_detail'),
    url(r'^live-music/$', views.live_music, name='live_music'),
    url(r'^art-exhibitions/$', views.art_exhibition, name='art_exhibition'),
    url(r'^craft-markets/$', views.craft_market, name='craft_market'),
    url(r'^special-events/$', views.special_events, name='special_events'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
]
