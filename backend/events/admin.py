from django.contrib import admin
from .models import Event
from .models import Partner
from .models import Picture

admin.site.register(Event)
admin.site.register(Partner)
admin.site.register(Picture)