# -*- coding: utf-8 -*-
__author__ = 'Administrator'
from django import forms
from CMDB import models
from django.contrib.auth.models import User
import os,django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE","project_name.settings")
django.setup()
# def mobile_validate(value):
#     mobile_re = re.compile(r'^(13[0-9]|15[0-9]|17[678]|18[0-9]|14[57])[0-9]{8}$')
#     if not mobile_re.match(str(value)):
#         raise forms.ValidationError({'phone':str("手机号码格式错误")})


class sign_in(forms.Form):
    username = forms.CharField(max_length=20,error_messages={"required":"账号不能为空","max_length":"账号过长"})
    password1 = forms.CharField(min_length=4,widget=forms.PasswordInput,error_messages={"required":'密码不能为空',"invalid":'密码格式错误',"min_length":'密码长度要大于4位'})
    password2 = forms.CharField(min_length=4,widget=forms.PasswordInput,error_messages={"required":'确认密码不能为空',"invalid":'密码格式错误',"min_length":'密码长度要大于4位'})
    department = forms.CharField(max_length=64,error_messages={"required":'部门不能为空',"max_length":'输入过长'})
    email = forms.EmailField(error_messages={"required":'邮箱不能为空',"invalid":'邮箱格式错误'})
    phone = forms.IntegerField(error_messages={"required":'手机号码不能为空'})
    last_name = forms.CharField(max_length=20,error_messages={"required":"姓不能为空","max_length":"姓输入过长"})
    first_name = forms.CharField(max_length=20,error_messages={"required":"名字不能为空","max_length":"名字输入过长"})
    sex = forms.CharField(error_messages={"required":"请选择性别"})

    def clean(self):
    #     # if self.is_valid():
            cleaned_data = self.cleaned_data
            errors = {}
            password1 = cleaned_data.get('password1')
            password2 = cleaned_data.get('password2')
            username = cleaned_data.get('username')
    #         name = models.UserInfo.objects.filter(username=username)
            userfilter = User.objects.filter(username=username)
            print("userfilter",userfilter)
    #         if name:
    #             errors['username'] = '用户名已存在'
            if len(userfilter) > 0:
                errors['username'] = '用户名已存在'
            mobile_value = str(cleaned_data.get('phone'))
            mobile_re = re.compile(r'^(13[0-9]|15[0-9]|17[678]|18[0-9]|14[57])[0-9]{8}$')
            print("mobile_val",mobile_value)
            if mobile_value != "None" and not mobile_re.match(mobile_value):
                errors['phone'] = '手机号码格式错误'
            if password2 != password1:
                errors['password2'] = '二次输入密码不一致'
            if len(errors) != 0:
                print("form_errors",errors)
                raise forms.ValidationError(errors)
            return cleaned_data



class server_input(forms.Form):
    ip = forms.GenericIPAddressField(error_messages={"required":"IP不能为空","invalid":"IP格式错误"})
    model = forms.CharField(max_length=256,error_messages={"required":"请输入设备型号","max_length":"输入过长"})
    manufacture = forms.CharField(max_length=128,error_messages={"required":"请输入厂家","max_length":"输入过长"})
    sn = forms.CharField(max_length=256,error_messages={"required":"请输入SN号","max_length":"输入过长"})
    os_platform = forms.CharField(max_length=128,error_messages={"required":"","max_length":"输入过长"})
    os_version = forms.CharField(max_length=128,error_messages={"required":"","max_length":"输入过长"})
    cpu = forms.CharField(max_length=64,error_messages={"required":"请输入CPU型号","max_length":"输入过长"})
    cpu_physical_count = forms.IntegerField(error_messages={"required":"输入类型错误"})
    cpu_count = forms.IntegerField(error_messages={"required":"输入类型错误"})
    mem = forms.CharField(max_length=256,error_messages={"required":"请输入内存型号","max_length":"输入过长"})
    mem_val = forms.FloatField(error_messages={"required":"请输入内存大小","invalid":"请输入数字"})
    asset_id = forms.IntegerField(error_messages={"required":"请选择所属资产"})

class server_change(forms.Form):
    ip = forms.GenericIPAddressField(error_messages={"required":"IP不能为空","invalid":"IP格式错误"})
    model = forms.CharField(max_length=256,error_messages={"required":"请输入设备型号","max_length":"输入过长"})
    manufacture = forms.CharField(max_length=128,error_messages={"required":"请输入厂家","max_length":"输入过长"})
    sn = forms.CharField(max_length=256,error_messages={"required":"请输入SN号","max_length":"输入过长"})
    os_platform = forms.CharField(max_length=128,error_messages={"required":"","max_length":"输入过长"})
    os_version = forms.CharField(max_length=128,error_messages={"required":"","max_length":"输入过长"})
    cpu = forms.CharField(max_length=64,error_messages={"required":"请输入CPU型号","max_length":"输入过长"})
    cpu_physical_count = forms.IntegerField(error_messages={"required":"输入类型错误"})
    cpu_count = forms.IntegerField(error_messages={"required":"输入类型错误"})
    mem = forms.CharField(max_length=256,error_messages={"required":"请输入内存型号","max_length":"输入过长"})
    mem_val = forms.FloatField(error_messages={"required":"请输入内存大小","invalid":"请输入数字"})
    asset_id = forms.IntegerField(error_messages={"required":"请选择所属资产"})
    old_ip = forms.GenericIPAddressField(error_messages={"required":"IP不能为空","invalid":"IP格式错误"})

    def clean(self):
        cleaned_data = self.cleaned_data
        print("form_clean_data",cleaned_data)
        errors = {}
        old_ip = cleaned_data.get('old_ip')
        new_ip = cleaned_data.get('ip')
        print("OLD_IP",old_ip,"NEW_IP",new_ip)
        try:
            ip = models.ServerInfo.objects.filter(ip=new_ip).values()[0]['ip']
        except:
            ip = None
        print("IP111",ip)
        if ip and ip != old_ip:
            errors['ip'] = "IP已存在"
        if len(errors) != 0:
            raise forms.ValidationError(errors)
        return cleaned_data



class idc_input(forms.Form):
    name = forms.CharField(max_length=256,error_messages={"required":"输入机房名称","max_length":"输入过长"})
    address = forms.CharField(max_length=256,error_messages={"required":"","max_length":"输入过长"})
    telphone = forms.IntegerField(error_messages={"required":"联系电话不能为空"})

class bussiness_input(forms.Form):
    name = forms.CharField(max_length=256,error_messages={"required":"业务线不能为空","max_length":"输入过长"})

class asset_input(forms.Form):
    device_type_id=forms.IntegerField(error_messages={"required":"请选择设备类型"})
    device_status_id=forms.IntegerField(error_messages={"required":"请选择状态"})
    cabinet_num=forms.CharField(empty_value=" ",max_length=30,error_messages={"required":"请输入机柜号","max_length":"输入过长"})
    cabinet_order=forms.CharField(empty_value=" ",max_length=30,error_messages={"required":"请输入机柜中序号","max_length":"输入过长"})
    idc=forms.CharField(error_messages={"required":"请选择机房"})
    bussiness_unit=forms.CharField(error_messages={"required":"请选择业务线"})

    def clean(self):
        cleaned_data =self.cleaned_data
        errors = {}
        idc = cleaned_data.get('idc')
        cabinet_num = cleaned_data.get('cabinet_num')
        cabinet_order = cleaned_data.get('cabinet_order')
        try:
            aa = models.asset.objects.filter(idc=idc,cabinet_num=cabinet_num,cabinet_order=cabinet_order)
        except:
            aa = None
        if aa:
            errors['cabinet_order'] = '该机柜位置已占用'
        if len(errors) != 0:
                raise forms.ValidationError(errors)
        return cleaned_data


class asset_change(forms.Form):
    device_type_id=forms.IntegerField(error_messages={"required":"请选择设备类型"})
    device_status_id=forms.IntegerField(error_messages={"required":"请选择状态"})
    cabinet_num=forms.CharField(empty_value=" ",max_length=30,error_messages={"required":"请输入机柜号","max_length":"输入过长"})
    cabinet_order=forms.CharField(empty_value=" ",max_length=30,error_messages={"required":"请输入机柜中序号","max_length":"输入过长"})
    idc=forms.CharField(error_messages={"required":"请选择机房"})
    bussiness_unit=forms.CharField(error_messages={"required":"请选择业务线"})
    id=forms.IntegerField()

    def clean(self):
        cleaned_data =self.cleaned_data
        errors = {}
        id = cleaned_data.get('id')
        old_idc = models.asset.objects.filter(id=id).values()[0]['idc_id']
        old_cabinet_num = models.asset.objects.filter(id=id).values()[0]['cabinet_num']
        old_cabinet_order = models.asset.objects.filter(id=id).values()[0]['cabinet_order']
        old_k = str(old_idc)+"_"+old_cabinet_num+"_"+old_cabinet_order
        idc = cleaned_data.get('idc')
        cabinet_num = cleaned_data.get('cabinet_num')
        cabinet_order = cleaned_data.get('cabinet_order')
        new_k = idc+"_"+cabinet_num+"_"+cabinet_order
        aa = models.asset.objects.filter(idc=idc,cabinet_num=cabinet_num,cabinet_order=cabinet_order)
        if aa and new_k!=old_k:
            errors['cabinet_order'] = '该机柜位置已占用'
        if len(errors) != 0:
                raise forms.ValidationError(errors)
        return cleaned_data