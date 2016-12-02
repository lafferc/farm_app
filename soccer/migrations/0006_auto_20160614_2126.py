# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0005_add_euro2016_matches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='code',
            field=models.CharField(unique=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='match',
            unique_together=set([('tournament', 'match_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='prediction',
            unique_together=set([('user', 'match')]),
        ),
    ]
