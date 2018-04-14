from django.contrib import admin

# Register your models here.
from .models import Location,Homes,Agency

admin.site.register(Location)
admin.site.register(Homes)
admin.site.register(Agency)