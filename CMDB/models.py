# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField('用户名',max_length=32,primary_key=True)
    password = models.CharField('密码',max_length=32)
    department = models.CharField('部门',max_length=100)
    email = models.EmailField('邮箱',null=True)
    phone = models.CharField('电话',max_length=11,null=True)
    class Meta:
        verbose_name="用户信息"
        verbose_name_plural="用户信息"
    def __str__(self):
        return self.username


class BusinessUnit(models.Model):
    '''
    业务线表
    '''
    name = models.CharField('业务线',max_length=64,unique=True)
    class Meta:
        verbose_name_plural='业务信息'
        verbose_name='业务信息'
    def __str__(self):
        return self.name


class DataCenter(models.Model):
    name = models.CharField('机房名称',max_length=128,unique=True)
    address = models.CharField('地址',max_length=256,null=True)
    telphone = models.CharField('联系电话',max_length=15,null=True)
    class Meta:
        verbose_name="机房信息"
        verbose_name_plural="机房信息"
    def __str__(self):
        return self.name

class asset(models.Model):
    '''
    资产信息表
    '''
    device_type_choices = (
        (1,'服务器'),
        (2,'交换机'),
        (3,'防火墙'),
    )
    device_status_choices = (
        (1,'上架'),
        (2,'在线'),
        (3,'离线'),
        (4,'下架'),
    )
    device_type_id = models.IntegerField(choices=device_type_choices,default=1)
    device_status_id = models.IntegerField(choices=device_status_choices,default=1)
    cabinet_num = models.CharField('机柜号',max_length=30,null=True,blank=True)
    cabinet_order = models.CharField('机柜中序号',max_length=30,null=True,blank=True)
    idc = models.ForeignKey('DataCenter',verbose_name='机房',null=True,blank=True)
    bussiness_unit = models.ForeignKey('BusinessUnit',verbose_name='属于的业务线',null=True,blank=True)

    class Meta:
        verbose_name_plural='资产信息'
        verbose_name='资产信息'
    def __str__(self):
        return "%s-%s-%s" %(self.idc.name,self.cabinet_num,self.cabinet_order)


class ServerInfo(models.Model):
    asset = models.OneToOneField('asset')
    ip = models.GenericIPAddressField('ip',unique=True)
    model = models.CharField('型号',max_length=256)
    manufacture = models.CharField('制造商',max_length=256)
    sn = models.CharField('SN号码',max_length=256)
    os_platform = models.CharField('系统平台',max_length=128)
    os_version = models.CharField('系统版本',max_length=128)
    cpu = models.CharField('CPU型号',max_length=64)
    cpu_physical_count = models.IntegerField('CPU数量')
    cpu_count = models.IntegerField('CPU核心数量')
    mem = models.CharField('内存型号',max_length=256)
    mem_val = models.FloatField('内存大小',max_length=5)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name='服务器信息'
        verbose_name_plural='服务器信息'
    def __str__(self):
        return self.ip


