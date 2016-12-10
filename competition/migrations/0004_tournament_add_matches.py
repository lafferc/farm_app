# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0003_sport_add_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='add_matches',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
