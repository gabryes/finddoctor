# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=80, verbose_name='Sobrenome')),
            ],
        ),
    ]