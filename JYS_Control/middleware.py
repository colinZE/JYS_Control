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

# EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
A=['/login/','/login','/sign_in/','/sign_in','/admin/','/admin/login/','/favicon.ico']

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("PATH", request.path)
        sessionid = request.COOKIES.get('sessionid',None)
        # print("time_now",time_now,type(time_now))
        # print("expire_time",expire_time,type(expire_time))
        if request.path not in A:
            time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
            # try:
            #     print("1")
            #     user = models.DjangoSession.objects.filter(session_key=sessionid)
            # except:
            #     print("2")
            #     user = None
            try:
                expire_time = models.DjangoSession.objects.filter(session_key=sessionid).values()[0]['expire_date'].strftime("%Y-%m-%d %H:%I:%S")
            except:
                expire_time = None
            print("expire_time",expire_time)
            # print("user",user)
            # if request.session.get('user', None):
            #     print("suser_id", request.session.get('user'))
            #     print("session_id", request.session.get('SESSION'))
            #     print("00000", request.COOKIES.get('sessionid',None))
            #     pass
            if expire_time and time_now < expire_time:
                print("ok")
                pass
            else:
                print("session无效")
                return HttpResponseRedirect('/login/')
        else:
            pass