'''
This file is used to register the models in the admin panel.
See https://docs.djangoproject.com/en/3.2/ref/contrib/admin/ for more information.
'''
from django.contrib import admin
from .models import Tender

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'euro_value', 'btc')