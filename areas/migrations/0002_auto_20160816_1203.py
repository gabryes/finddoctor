# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-16 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': 'Área', 'verbose_name_plural': 'Áreas'},
        ),
        migrations.AlterField(
            model_name='area',
            name='nomeArea',
            field=models.CharField(default='Medico', max_length=80, verbose_name='Profissão'),
        ),
    ]
