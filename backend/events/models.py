from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_banner = models.ImageField()
    event_background = models.ImageField()
    event_pictures = models.ForeignKey('Picture', on_delete=models.CASCADE)
    event_description = models.TextField(max_length=500)
    event_partners = models.ForeignKey('Partner', on_delete=models.PROTECT)
    event_google_form = models.TextField()

    # maybe we should make our own registrations with automatic delete?

    def __unicode__(self):
        return self.title


class Partner(models.Model):
    partner_name = models.CharField(max_length=50)
    partner_image = models.ImageField()

    def __unicode__(self):
        return self.title


class Picture(models.Model):
    picture = models.ImageField()

    def __unicode__(self):
        return self.title
