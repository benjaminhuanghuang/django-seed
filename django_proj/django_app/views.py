# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404

from django_app.models import Items


# Create your views here.
def index(request):
    items = Items.objects.exclude(quantity=0)
    # return HttpResponse('<p>This is the index view </p>')
    return render(request, 'django_app/index.html', {'items': items})


# r'^item/(?P<id>\d+)'
def item_detail(request, id):
    # return HttpResponse('<p>This is the item_detail view with id {0} </p>'.format(id))
    try:
        item = Items.objects.get(id= id)
    except Items.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'django_app/item_detail.html', {'item': item})