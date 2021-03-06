from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_banner = models.ImageField(blank=True, upload_to="events/general_pictures")
    event_background = models.ImageField(
        blank=True, upload_to="events/general_pictures"
    )
    event_pictures = models.ManyToManyField("Picture", blank=True)
    event_description = models.TextField(max_length=500)
    event_partners = models.ManyToManyField("Partner", blank=True)
    event_google_form = models.TextField(blank=True)

    # maybe we should make our own registrations with automatic delete?

    def __str__(self):
        return self.event_name

    def __unicode__(self):
        return self.event_name


class Partner(models.Model):
    partner_name = models.CharField(max_length=50)
    partner_image = models.ImageField(upload_to="events/partner_images")

    def __str__(self):
        return self.partner_name


class Picture(models.Model):
    picture_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="events/pictures")

    def __str__(self):
        return self.picture_name
