# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
import models


# Create your views here.


'''
id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=32)
    sn = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    comment = models.CharField(max_length=32)
'''

def index(request):
    #return HttpResponse("Hello World!")

    if request.method == "POST":
        name = request.POST.get("name", None)
        sn = request.POST.get("sn", None)
        category = request.POST.get("category", None)
        status = request.POST.get("status", None)
        comment = request.POST.get("comment", None)
        models.AssetInfo.objects.create(name=name, sn=sn, category=category, status=status, comment=comment)

    asset_all = models.AssetInfo.objects.all()

    return render(request, "index.html", {"asset_list":asset_all})

def search(request):
    return render(request, "search.html")