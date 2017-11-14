# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-01 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u4e1a\u52a1\u7ebf')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u4fe1\u606f',
                'verbose_name_plural': '\u4e1a\u52a1\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name='ip')),
                ('model', models.CharField(max_length=256, verbose_name='\u578b\u53f7')),
                ('manufacture', models.CharField(max_length=256, verbose_name='\u5236\u9020\u5546')),
                ('sn', models.CharField(max_length=256, verbose_name='SN\u53f7\u7801')),
                ('os_platform', models.CharField(max_length=128, verbose_name='\u7cfb\u7edf\u5e73\u53f0')),
                ('os_version', models.CharField(max_length=128, verbose_name='\u7cfb\u7edf\u7248\u672c')),
                ('cpu', models.CharField(max_length=64, verbose_name='CPU\u578b\u53f7')),
                ('cpu_physical_count', models.IntegerField(verbose_name='CPU\u6570\u91cf')),
                ('cpu_count', models.IntegerField(verbose_name='CPU\u6838\u5fc3\u6570\u91cf')),
                ('mem', models.CharField(max_length=256, verbose_name='\u5185\u5b58\u578b\u53f7')),
                ('mem_val', models.FloatField(max_length=5, verbose_name='\u5185\u5b58\u5927\u5c0f')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668\u4fe1\u606f',
                'verbose_name_plural': '\u670d\u52a1\u5668\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('username', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=32, verbose_name='\u5bc6\u7801')),
                ('department', models.CharField(max_length=100, verbose_name='\u90e8\u95e8')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='\u90ae\u7bb1')),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='\u7535\u8bdd')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
    ]
