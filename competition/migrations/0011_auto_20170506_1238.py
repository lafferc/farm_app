# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import competition.models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0010_tournament_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='state',
            field=models.IntegerField(default=1, choices=[(0, b'Pending'), (1, b'Active'), (2, b'finished'), (3, b'archived')]),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='year',
            field=models.IntegerField(default=competition.models.current_year, choices=[(2016, 2016), (2017, 2017)]),
        ),
    ]
