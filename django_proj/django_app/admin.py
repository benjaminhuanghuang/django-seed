# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Items


# used for django admin to display item on web page
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity']

# Register your models here.
admin.site.register(Items, ItemsAdmin)
