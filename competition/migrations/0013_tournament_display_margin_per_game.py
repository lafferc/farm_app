# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0012_auto_20170507_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='display_margin_per_game',
            field=models.BooleanField(default=False),
        ),
    ]
