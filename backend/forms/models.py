from django.db import models


# Create your models here

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.partner_name

