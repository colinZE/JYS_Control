# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from CMDB import models
from django.contrib import admin

# Register your models here.
admin.site.register(models.UserInfo)
admin.site.register(models.asset)
admin.site.register(models.BusinessUnit)
admin.site.register(models.DataCenter)
admin.site.register(models.ServerInfo)