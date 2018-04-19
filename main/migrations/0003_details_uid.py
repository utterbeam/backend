# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_details_idd'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='uid',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
