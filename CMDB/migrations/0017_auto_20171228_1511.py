# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-28 07:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0016_userinfo'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userinfo',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_permissions',
        ),
    ]