from django.contrib import admin
from chat import models

# Register your models here.
admin.site.register(models.Room)
admin.site.register(models.Message)