# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0005_auto_20170426_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='draw_bonus',
            field=models.DecimalField(default=1, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='bonus',
            field=models.DecimalField(default=2, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='late_get_bonus',
            field=models.BooleanField(default=False),
        ),
    ]
