# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0006_auto_20170501_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='match_start_verb',
            field=models.CharField(default=b'Kick Off', max_length=50),
        ),
        migrations.AddField(
            model_name='sport',
            name='scoring_unit',
            field=models.CharField(default=b'point', max_length=50),
        ),
        migrations.AlterField(
            model_name='match',
            name='kick_off',
            field=models.DateTimeField(verbose_name=b'Start Time'),
        ),
    ]
