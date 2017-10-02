from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):

    changefreq = 'weekly'
    
    def items(self):
        return ['index', 'live_music', 'art_exhibition', 'craft_market', 'special_events']

    def location(self, item):
        return reverse(item)