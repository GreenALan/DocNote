# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 08:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20161209_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docs',
            name='treenode',
        ),
    ]
