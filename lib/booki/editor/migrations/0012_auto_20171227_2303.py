# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-12-27 23:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0011_auto_20171227_2214_remove_duplicated_statuses'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookstatus',
            unique_together=set([('book', 'name')]),
        ),
    ]
