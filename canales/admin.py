from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Chat, Mensaje

admin.site.register(Chat)
admin.site.register(Mensaje)
