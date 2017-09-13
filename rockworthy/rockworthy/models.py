from django.db import models

class EventHost(models.Model):
    
    host_name = models.CharField(max_length=255)
    host_area = models.CharField(max_length=255)
    host_address = models.TextField(max_length=1001)
    host_image = models.ImageField(upload_to='rockworthy/static/assets/event_hosts/main_photo', max_length=255)
    host_id = models.CharField(max_length=255)

    def __str__(self):
        return  self.host_name

    class Meta:
        verbose_name = 'Event Host'
        verbose_name_plural = 'Event Hosts'