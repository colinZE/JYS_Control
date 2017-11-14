__author__ = 'Administrator'
import os,django
from CMDB import models
os.environ.update({"DJANGO_SETTINGS_MODULE":"JYS_Control.settings"})
django.setup()
models.UserInfo.objects.all()

