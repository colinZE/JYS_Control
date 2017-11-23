# -*- coding: utf-8 -*-
__author__ = 'Administrator'
from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile
from CMDB import models
import datetime
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("PATH", request.path)
        sessionid = request.COOKIES.get('sessionid',None)
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
        try:
            expire_time = models.DjangoSession.objects.filter(session_key=sessionid).values()[0]['expire_date'].strftime("%Y-%m-%d %H:%I:%S")
        except:
            expire_time = None
        # print("time_now",time_now,type(time_now))
        # print("expire_time",expire_time,type(expire_time))
        if request.path != '/login/':
            try:
                user = models.DjangoSession.objects.filter(session_key=sessionid)
            except:
                user = None
            # if request.session.get('user', None):
            #     print("suser_id", request.session.get('user'))
            #     print("session_id", request.session.get('SESSION'))
            #     print("00000", request.COOKIES.get('sessionid',None))
            #     pass
            if user and time_now < expire_time:
                pass
            else:
                print("session无效")
                return HttpResponseRedirect('/login/')
