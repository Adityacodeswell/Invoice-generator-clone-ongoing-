from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(ServiceProvider)