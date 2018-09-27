from django.contrib import admin
from .models import Person,Comment,Car,Manufacturer

admin.site.register([Person,Comment,Car,Manufacturer])
