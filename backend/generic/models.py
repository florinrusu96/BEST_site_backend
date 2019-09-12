from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from .core.signals import partner_removal_handler


"""
   # TODO
    - make image mandatory and add a default image
"""


class Partner(models.Model):
    name = models.CharField(max_length=64, unique=True)
    image = models.ImageField(default=None, upload_to='generic/images')

    def __str__(self):
        return self.name

post_delete.connect(partner_removal_handler, Partner)
