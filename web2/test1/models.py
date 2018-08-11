# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class AssetInfo(models.Model):
    name = models.CharField(max_length=32)
    sn = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    comment = models.CharField(max_length=32)