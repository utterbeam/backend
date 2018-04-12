# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(max_length=150, null=True, blank=True)),
                ('subText', models.CharField(max_length=150, null=True, blank=True)),
                ('writeup', models.CharField(max_length=1500, null=True, blank=True)),
                ('imageUrl', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
    ]
