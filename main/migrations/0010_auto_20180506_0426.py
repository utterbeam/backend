# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20180506_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer_work',
            name='matched_keyword',
            field=models.ManyToManyField(related_name='matched_keyword', null=True, to='main.keywords'),
        ),
        migrations.AlterField(
            model_name='employer_work',
            name='keywords_selected',
            field=models.ManyToManyField(related_name='keywords_selected', null=True, to='main.keywords'),
        ),
    ]
