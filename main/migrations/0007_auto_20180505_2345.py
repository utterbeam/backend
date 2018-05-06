# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_employer_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer_work',
            name='assigned_writer',
            field=models.OneToOneField(related_name='writer', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer_work',
            name='work_description',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employer_work',
            name='user',
            field=models.OneToOneField(related_name='employer', to=settings.AUTH_USER_MODEL),
        ),
    ]
