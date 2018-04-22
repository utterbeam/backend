# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='write_up',
            fields=[
                ('url', models.CharField(max_length=150, null=True, blank=True)),
                ('post_id', models.AutoField(serialize=False, primary_key=True)),
                ('heading', models.CharField(max_length=150, null=True, blank=True)),
                ('sub_text', models.CharField(max_length=150, null=True, blank=True)),
                ('writeup', models.CharField(max_length=1500, null=True, blank=True)),
                ('image_url', models.CharField(max_length=200, null=True, blank=True)),
                ('upvotes', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]
