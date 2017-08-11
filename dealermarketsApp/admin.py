from django.contrib import admin

# Register your models here.

from .models import Dealer, Client

admin.site.register(Dealer)
admin.site.register(Client)