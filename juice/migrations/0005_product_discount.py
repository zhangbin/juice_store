# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-05 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juice', '0004_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
