"""JYS_Control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from CMDB import views

urlpatterns = [
    url(r'^CMDB/$', views.CMDB),
    url(r'^server_info', views.server_info),
    url(r'^server_input',views.server_input),
    url(r'^server_change',views.server_change),
    url(r'^asset_info',views.asset_info),
    url(r'^asset_input',views.asset_input),
    url(r'^asset_change',views.asset_change),
    url(r'^idc_input',views.idc_input),
    url(r'^idc_change',views.idc_change),
    url(r'^bussiness_input',views.bussiness_input),
    url(r'^bussiness_change',views.bussiness_change),
    url(r'^$',views.CMDB)
]
