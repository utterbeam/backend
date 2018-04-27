# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180426_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='write_up',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 27, 4, 0, 43, 541975, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='write_up',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 27, 4, 0, 48, 939631, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
