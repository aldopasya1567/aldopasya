# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-09-04 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lenkap', models.CharField(max_length=255)),
                ('judul', models.CharField(max_length=255)),
                ('isi', models.TextField()),
                ('penulis', models.CharField(max_length=255)),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
    ]
