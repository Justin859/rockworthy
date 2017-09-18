from django.db import models

class EventHost(models.Model):
    
    host_name = models.CharField(max_length=255)
    host_area = models.CharField(max_length=255)
    host_address = models.TextField(max_length=1001)
    host_image = models.ImageField(upload_to='rockworthy/static/assets/event_hosts/main_photo', max_length=255)
    host_id = models.CharField(max_length=255)

    EVENT_TYPES = (('Live Shows', 'Live Shows'), ('Art Exhibition', 'Art Exhibition'), ('Craft Market', 'Craft Market'))

    event_type = models.CharField(max_length=14, choices=EVENT_TYPES, default='Live Shows')

    HOST_TYPES = (('Special Event', 'Special Event'), ('Venue', 'Venue'))

    host_type = models.CharField(max_length=13, choices=HOST_TYPES, default='Venue')

    def __str__(self):
        return  self.host_name

    class Meta:
        verbose_name = 'Event Host'
        verbose_name_plural = 'Event Hosts'