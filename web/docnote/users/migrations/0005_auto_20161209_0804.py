# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_docs_treenode'),
    ]

    operations = [
        migrations.AddField(
            model_name='docs',
            name='owner',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docs',
            name='treenodeid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sorttree',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sorttree',
            name='owner',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sorttree',
            name='parendid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
