# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180505_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer_work',
            name='assigned_writer',
            field=models.ForeignKey(related_name='writer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employer_work',
            name='user',
            field=models.ForeignKey(related_name='employer', to=settings.AUTH_USER_MODEL),
        ),
    ]
