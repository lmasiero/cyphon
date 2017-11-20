# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 17:43
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0011_auto_20170815_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('alert', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='alerts.Alert')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('notes', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
            ],
            options={
                'permissions': (('view_alert', 'Can see existing alerts'),),
                'verbose_name_plural': 'analyses',
            },
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
