# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-04 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_translationproject', '0003_realpath_can_be_none'),
        ('pootle_app', '0010_obsolete_path_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory',
            name='tp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dirs', to='pootle_translationproject.TranslationProject'),
        ),
    ]
