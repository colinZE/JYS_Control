# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from CMDB import models
from CMDB import forms
import json
from django.shortcuts import render,redirect,HttpResponseRedirect


# Create your views here.
#首页
def index(request):


    return render(request, 'index.html')


def CMDB(request):
    return render(request, 'CMDB.html')


def asset_info(request):
    device_type_list=["","服务器","交换机","防火墙"]
    device_status_list=["","上架","在线","离线","下架"]
    asset_info_obj=models.asset.objects.all().values()
    for i in asset_info_obj:
        i['device_type_id']=device_type_list[i['device_type_id']]
        i['device_status_id']=device_status_list[i['device_status_id']]
        idc_obj=models.DataCenter.objects.filter(id=i['idc_id']).values()[0]
        i['idc_id']=idc_obj['name']
        bussiness_obj=models.BusinessUnit.objects.filter(id=i['bussiness_unit_id']).values()[0]
        i['bussiness_unit_id']=bussiness_obj['name']
        i['name']=idc_obj['name']+"-"+i['cabinet_num']+"-"+i['cabinet_order']
        try:
            server_obj=models.ServerInfo.objects.filter(asset_id=i['id']).values()[0]
            i['device_ip']=server_obj['ip']
        except:
            i['device_ip']=""
    print(asset_info_obj)
    return render(request,'data_input/asset_info.html',{'asset_info_obj':asset_info_obj})



def asset_input(request):
    # if request.method == 'POST':
    #     bussiness_info_obj=models.BusinessUnit.objects.all().values()
    #     bussiness_info_dic={}
    #     # print("111111111",bussiness_info_obj,type(bussiness_info_obj))
    #     for i in bussiness_info_obj:
    #         j=i["name"]
    #         bussiness_info_dic[j]=i
    #     bussiness_info_dic1=json.dumps(bussiness_info_dic,ensure_ascii=False)
    #     # print("222222222",bussiness_info_dic1,type(bussiness_info_dic1))
    #     return HttpResponse(bussiness_info_dic1)
    if request.method == 'POST':
        jdata=request.POST.dict()
        data = forms.asset_input(jdata)
        print("DATA",data)
        if data.is_valid():
            clean_data = data.clean()
            print("CLEANED",clean_data,type(clean_data))
            idc_id=clean_data['idc']
            idc_obj=models.DataCenter.objects.get(id=idc_id)
            bussiness_id=clean_data['bussiness_unit']
            bussiness_obj=models.BusinessUnit.objects.get(id=bussiness_id)
            print('IDC_OBJ',idc_obj,type(idc_obj),'BUSS_OBJ',bussiness_obj)
            clean_data['idc']=idc_obj
            clean_data['bussiness_unit']=bussiness_obj
            print("CLEANED2",clean_data)
            asset_info_obj=models.asset(**clean_data)
            asset_info_obj.save()
            succ=json.dumps({'succ':'ok'})
            return HttpResponse(succ)
        else:
            err = data.errors
            print("ERROR",type(err),err)
            error_msg={}
            for i in err:
                for j in err[i]:
                    error_msg[i]=j
            error_msg_dic=json.dumps(error_msg,ensure_ascii=False)
            print("ERROR_DIC",type(error_msg_dic),error_msg_dic)
            return HttpResponse(error_msg_dic)

    idc_info_obj=models.DataCenter.objects.all()
    bussiness_info_obj=models.BusinessUnit.objects.all()
    return render(request,'data_input/asset_input.html',{"idc_info_obj":idc_info_obj,"bussiness_info_obj":bussiness_info_obj})


#资产信息修改
def asset_change(request):
    if request.method == 'POST':
        jdata=request.POST.dict()
        print("JDATA",jdata)
        if jdata['shanchu']=="1":
            id=jdata['id']
            models.asset.objects.filter(id=id).delete()
            succ=json.dumps({'succ':'ok'})
            return HttpResponse(succ)
        else:
            data = forms.asset_change(jdata)
            print("DATA",data)
            if data.is_valid():
                clean_data = data.clean()
                print("CLEANED",clean_data)
                id=jdata['id']
                models.asset.objects.filter(id=id).update(**clean_data)
                succ=json.dumps({'succ':'ok'})
                return HttpResponse(succ)
            else:
                err = data.errors
                print("ERROR",err,"type123",type(data))
                error_msg={}
                for i in err:
                    for j in err[i]:
                        error_msg[i]=j
                error_msg_dic=json.dumps(error_msg,ensure_ascii=False)
                print("ERROR_DIC",type(error_msg_dic),error_msg_dic)
                return HttpResponse(error_msg_dic)


    r="url",request.get_full_path()
    print('r',r)
    print("url_canshu",request.get_raw_uri())
    asset_id=request.GET.get('asset_id')
    print("ASSET",asset_id)
    asset_read_obj=models.asset.objects.filter(id=asset_id).values()[0]
    print("asset",asset_read_obj,"TYPE",type(asset_read_obj))
    idc_info_obj=models.DataCenter.objects.all()
    bussiness_info_obj=models.BusinessUnit.objects.all()
    return render(request,'data_input/asset_change.html',{"idc_info_obj":idc_info_obj,"bussiness_info_obj":bussiness_info_obj,"asset_read_obj":asset_read_obj})




#机房信息录入
def idc_input(request):
    if request.method == 'POST':
        jdata=request.POST.dict()
        data = forms.idc_input(jdata)
        # print("123456789",data,"type123",type(data))
        if data.is_valid():
            clean_data = data.clean()
            print('idc_input_cleandata',clean_data)
            idc_obj = models.DataCenter(**clean_data)
            idc_obj.save()
            succ=json.dumps({'succ':'ok'})
            return HttpResponse(succ)
        else:
            err = data.errors
            print("ERROR",err,"type123",type(data))
            error_msg={}
            for i in err:
                for j in err[i]:
                    error_msg[i]=j
            error_msg_dic=json.dumps(error_msg,ensure_ascii=False)
            print("ERROR_DIC",type(error_msg_dic),error_msg_dic)
            return HttpResponse(error_msg_dic)
    return render(request,'data_input/idc_input.html')

#机房信息修改
def idc_change(request):
    if request.method == 'POST':
        jdata=request.POST.dict()
        print("JDATA",jdata,type(jdata))
        if jdata['shanchu'] == "1":
            succ=json.dumps({'succ':'ok'})
            return HttpResponse(succ)
        else:
            data = forms.idc_input(jdata)
            print("DATA",data,"type123",type(data))
            if data.is_valid():
                clean_data = data.clean()
                print('idc_input_cleandata',clean_data)
                id=jdata['id']
                models.DataCenter.objects.filter(id=id).update(**clean_data)

                succ=json.dumps({'succ':'ok'})
                return HttpResponse(succ)
            else:
                err = data.errors
                print("ERROR",err,"type123",type(data))
                error_msg={}
                for i in err:
                    for j in err[i]:
                        error_msg[i]=j
                error_msg_dic=json.dumps(error_msg,ensure_ascii=False)
                print("ERROR_DIC",type(error_msg_dic),error_msg_dic)
                return HttpResponse(error_msg_dic)
    r="url",request.get_full_path()

    print('r',r)
    print("url_canshu",request.get_raw_uri())
    idc=request.GET.get('idc')
    idc_read_obj=models.DataCenter.objects.filter(id=idc).values()[0]
    print(idc_read_obj,type(idc_read_obj))
    return render(request,'data_input/idc_change.html',{"idc_read_obj":idc_read_obj})


#业务线录入
def bussiness_input(request):
    if request.method == 'POST':
        jdata = request.POST.dict()
        data = forms.bussiness_input(jdata)
        if data.is_valid():
            clean_data = data.clean()
            print("buss_clean_data",clean_data)
            bussiness_obj = models.BusinessUnit(**clean_data)
            bussiness_obj.save()
            succ=json.dumps({'succ':'ok'})
            return HttpResponse(succ)
        else:
            err = data.errors
            print("error",err)
            err_msg = {}
            for i in err:
                for j in err[i]:
                    err_msg[i]=j
            err_msg_dic=json.dumps(err_msg,ensure_ascii=False)
            return HttpResponse(err_msg_dic)
    return render(request,'data_input/bussiness_input.html')



#业务线修改
def bussiness_change(request):
    if request.method == 'POST':
        jdata = request.POST.dict()
        print("JDATA",jdata)
        if jdata['shanchu']== "1":
            id = jdata['id']
            models.BusinessUnit.objects.filter(id=id).delete()
            succ=json.dumps({'succ':'ok'})
            return HttpResponse(succ)
        else:
            data = forms.bussiness_input(jdata)
            if data.is_valid():
                clean_data = data.clean()
                print("buss_clean_data",clean_data)
                id=jdata["id"]
                print("ID",id)
                models.BusinessUnit.objects.filter(id=id).update(**clean_data)
                succ=json.dumps({'succ':'ok'})
                return HttpResponse(succ)
            else:
                err = data.errors
                print("error",err)
                err_msg = {}
                for i in err:
                    for j in err[i]:
                        err_msg[i]=j
                err_msg_dic=json.dumps(err_msg,ensure_ascii=False)
                return HttpResponse(err_msg_dic)

    r="url",request.get_full_path()

    bussiness = request.GET.get('bussiness')
    bussiness_read_info = models.BusinessUnit.objects.filter(id=bussiness).values()[0]
    print("BUS",bussiness_read_info)
    return render(request,'data_input/bussiness_change.html',{"bussiness_read_info":bussiness_read_info})


#主机信息
def server_info(request):
    server_info_obj=models.ServerInfo.objects.all()
    return render(request, 'data_input/server_info.html',{'server_info_obj':server_info_obj})

#主机信息录入
def server_input(request):
    if request.method == 'POST':
        jdata=request.POST.dict()
        print('JDATA',jdata)
        data = forms.server_input(jdata)
        if data.is_valid():
            clean_data = data.clean()
            print('CLEAN_DATA',clean_data)
            ip=clean_data['ip']
            print('ip:',ip,'type:',type(ip))
            check_obj=models.ServerInfo.objects.filter(ip=ip)
            print('123456',check_obj)
            if not check_obj:
                server_obj = models.ServerInfo(**clean_data)
                server_obj.save()
                succ=json.dumps({'succ':'ok'})
                return HttpResponse(succ)
            else:
                error_msg={}
                error_msg['ip']="IP已存在"
                error_msg_dic=json.dumps(error_msg,ensure_ascii=False)
                print("ERROR_DIC",type(error_msg),error_msg_dic)
                return HttpResponse(error_msg_dic)

        else:
            err = data.errors
            print("ERROR",type(err),err)
            error_msg={}
            for i in err:
                for j in err[i]:
                    error_msg[i]=j
            error_msg_dic=json.dumps(error_msg,ensure_ascii=False)
            print("ERROR_DIC",type(error_msg_dic),error_msg_dic)
            return HttpResponse(error_msg_dic)

    asset_info_obj=models.asset.objects.all().values()
    for i in asset_info_obj:
        idc_obj=models.DataCenter.objects.filter(id=i['idc_id']).values()[0]

        i['name']=idc_obj['name']+"-"+i['cabinet_num']+"-"+i['cabinet_order']
    return render(request,'data_input/server_input.html',{"asset_info_obj":asset_info_obj})


def server_change(request):
    if request.method == 'POST':
        jdata=request.POST.dict()
        server_id=jdata['server_id']
        jdata['old_ip']=models.ServerInfo.objects.filter(id=server_id).values()[0]['ip']
        print("JDATA",jdata)
        if jdata['shanchu']=="1":
            models.ServerInfo.objects.filter(id=server_id).delete()
            succ=json.dumps({"succ":"ok"})
            return HttpResponse(succ)
        else:
            data = forms.server_change(jdata)
            if data.is_valid():
                clean_data = data.clean()
                del clean_data['old_ip']
                print("CLEANED",clean_data)
                models.ServerInfo.objects.filter(id=server_id).update(**clean_data)
                succ = json.dumps({"succ":"ok"})
                return HttpResponse(succ)
            else:
                err = data.errors
                error_msg={}
                for i in err:
                    for j in err[i]:
                        error_msg[i]=j
                error_msg_dic=json.dumps(error_msg,ensure_ascii=False)
                return HttpResponse(error_msg_dic)
    r="url",request.get_full_path()
    server_id = request.GET.get('server_id')
    print("url",server_id)
    server_read_obj=models.ServerInfo.objects.filter(id=server_id).values()[0]
    del server_read_obj['create_at']
    print("server_info",server_read_obj,"TYPE",type(server_read_obj))
    asset_info_obj=models.asset.objects.all().values()
    for i in asset_info_obj:
        idc_obj=models.DataCenter.objects.filter(id=i['idc_id']).values()[0]
        i['name']=idc_obj['name']+"-"+i['cabinet_num']+"-"+i['cabinet_order']
    return render(request,'data_input/server_change.html',{"asset_info_obj":asset_info_obj,"server_read_obj":server_read_obj})



#注册
def sign_in(request):
    if request.method == 'POST':
        jdata=request.POST.dict()
        print("JDATA",jdata,"TYPE",type(jdata))
        data = forms.sign_in(jdata)
        print("DATA111111",data)
        if data.is_valid():
            clean_data = data.clean()
            clean_data['password']=clean_data['password2']
            del(clean_data['password1'])
            del(clean_data['password2'])
            print('clean_data222222',clean_data)
            user_obj = models.UserInfo(**clean_data)
            user_obj.save()
            succ=json.dumps({'succ':'ok'})
            return HttpResponse(succ)

        else:
            err = data.errors
            print("TYPE",type(err))
            print("error3333333",err)
            error_msg={}
            for i in err:
                for j in err[i]:
                    error_msg[i]=j
                    print("JJJJJ",j,type(j))
            print(error_msg)
            error_msg_dic=json.dumps(error_msg,ensure_ascii=False)
            print(type(error_msg_dic),"dict_error",error_msg_dic)
            return HttpResponse(error_msg_dic)
    return render(request,'sign_in.html')


#登录

def login_view(request):
    if request.method == 'POST':
        print("111111",request.POST)
        username = request.POST.get('userName')
        password = request.POST.get('passWord')
        error_msg={}
        try:
            user = models.UserInfo.objects.get(username=username)
            print("USER",user)
            if password != user.password:
                error_msg['password']='密码错误'
            else:
                succ=json.dumps({'succ':'ok'})
                return HttpResponse(succ)
        except:
            error_msg['username']='用户不存在'

        error_msg_dic = json.dumps(error_msg,ensure_ascii=False)
        print(error_msg_dic)
        return HttpResponse(error_msg_dic)

    return render(request,'login.html')