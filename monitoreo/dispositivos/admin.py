from django.contrib import admin

# Register your models here.
from .models import Category,Zone,Organization,Device,Measurement,Alert

admin.site.register([Category,Zone,Organization,Device,Measurement,Alert])