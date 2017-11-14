# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-01 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type_id', models.IntegerField(choices=[(1, '\u670d\u52a1\u5668'), (2, '\u4ea4\u6362\u673a'), (3, '\u9632\u706b\u5899')], default=1)),
                ('device_status_id', models.IntegerField(choices=[(1, '\u4e0a\u67b6'), (2, '\u5728\u7ebf'), (3, '\u79bb\u7ebf'), (4, '\u4e0b\u67b6')], default=1)),
                ('cabinet_num', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u673a\u67dc\u53f7')),
                ('cabinet_order', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u673a\u67dc\u4e2d\u5e8f\u53f7')),
                ('bussiness_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CMDB.BusinessUnit', verbose_name='\u5c5e\u4e8e\u7684\u4e1a\u52a1\u7ebf')),
            ],
            options={
                'verbose_name': '\u8d44\u4ea7\u4fe1\u606f',
                'verbose_name_plural': '\u8d44\u4ea7\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='DataCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('address', models.CharField(max_length=256, null=True, verbose_name='\u5730\u5740')),
                ('telphone', models.CharField(max_length=15, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
            ],
            options={
                'verbose_name': '\u673a\u623f\u4fe1\u606f',
                'verbose_name_plural': '\u673a\u623f\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CMDB.DataCenter', verbose_name='\u673a\u623f'),
        ),
    ]
