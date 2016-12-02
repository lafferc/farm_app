# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0002_euro2016_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prediction',
            name='score',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='prediction',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
    ]
