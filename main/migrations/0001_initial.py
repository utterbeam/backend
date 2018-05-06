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
                ('image', models.FileField(upload_to=b'', blank=True)),
                ('image_url', models.CharField(max_length=200, null=True, blank=True)),
                ('author_id', models.AutoField(serialize=False, primary_key=True)),
                ('twitter', models.CharField(max_length=150, null=True, blank=True)),
                ('facebook', models.CharField(max_length=150, null=True, blank=True)),
                ('instagram', models.CharField(max_length=150, null=True, blank=True)),
                ('pinterest', models.CharField(max_length=150, null=True, blank=True)),
                ('blogs', models.CharField(max_length=250, null=True, blank=True)),
                ('url', models.CharField(max_length=150, null=True, blank=True)),
                ('fb_id', models.CharField(max_length=150, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='employer_work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_description', models.CharField(max_length=150, null=True, blank=True)),
                ('assigned_writer', models.OneToOneField(related_name='writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='keywords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sentiment_positive', models.CharField(max_length=200, null=True, blank=True)),
                ('sentiment_negative', models.CharField(max_length=200, null=True, blank=True)),
                ('sentiment_neutral', models.CharField(max_length=200, null=True, blank=True)),
                ('plagiarism', models.CharField(max_length=200, null=True, blank=True)),
                ('keywords_selected', models.ManyToManyField(to='main.keywords', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='employer_work',
            name='keywords_selected',
            field=models.ManyToManyField(to='main.keywords', null=True),
        ),
        migrations.AddField(
            model_name='employer_work',
            name='user',
            field=models.OneToOneField(related_name='employer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='author_detail',
            name='keywords_selected',
            field=models.ManyToManyField(to='main.keywords', null=True),
        ),
        migrations.AddField(
            model_name='author_detail',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
