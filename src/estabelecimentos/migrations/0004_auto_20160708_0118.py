# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-08 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimentos', '0003_auto_20160708_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='cnpj',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='CNPJ'),
        ),
    ]