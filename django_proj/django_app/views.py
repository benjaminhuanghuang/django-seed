# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<p>This is the index view </p>')

# r'^item/(?P<id>\d+)'
def item_detail(request, id):
    return HttpResponse('<p>This is the item_detail view with id {0} </p>'.format(id))