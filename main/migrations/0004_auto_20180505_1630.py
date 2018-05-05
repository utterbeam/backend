# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180427_0400'),
    ]

    operations = [
        migrations.CreateModel(
            name='keywords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='author_detail',
            name='keywords_selected',
            field=models.ManyToManyField(to='main.keywords', null=True),
        ),
        migrations.AddField(
            model_name='write_up',
            name='keywords_selected',
            field=models.ManyToManyField(to='main.keywords', null=True),
        ),
    ]
