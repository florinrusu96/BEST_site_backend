from django.db import models

# Create your models here.

class Partener(models.Model):
    name = models.CharField(max_length=64, unique=True)
    logo = models.ImageField()
    group = models.CharField(max_length=64)

    def __str__(self):
        return self.name
