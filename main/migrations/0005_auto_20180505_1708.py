# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180505_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='write_up',
            name='plagiarism',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='write_up',
            name='sentiment_negative',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='write_up',
            name='sentiment_neutral',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='write_up',
            name='sentiment_positive',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
