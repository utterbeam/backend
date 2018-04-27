# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author_detail',
            fields=[
                ('description', models.CharField(max_length=350, null=True, blank=True)),
                ('image', models.FileField(upload_to=b'imgs', blank=True)),
                ('image_url', models.CharField(max_length=200, null=True, blank=True)),
                ('author_id', models.AutoField(serialize=False, primary_key=True)),
                ('twitter', models.CharField(max_length=150, null=True, blank=True)),
                ('facebook', models.CharField(max_length=150, null=True, blank=True)),
                ('instagram', models.CharField(max_length=150, null=True, blank=True)),
                ('pinterest', models.CharField(max_length=150, null=True, blank=True)),
                ('blogs', models.CharField(max_length=250, null=True, blank=True)),
                ('url', models.CharField(max_length=150, null=True, blank=True)),
                ('fb_id', models.CharField(max_length=150, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
