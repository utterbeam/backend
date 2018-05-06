# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20180506_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer_work',
            name='assigned_writer',
            field=models.ForeignKey(related_name='writer', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
