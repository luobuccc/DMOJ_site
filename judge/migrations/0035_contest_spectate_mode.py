# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0034_submission_is_pretested'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestparticipation',
            name='spectate',
            field=models.BooleanField(default=False, help_text='', verbose_name='whether the user is spectating the contest'),
        ),
    ]
