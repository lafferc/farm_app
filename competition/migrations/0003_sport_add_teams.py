# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0002_auto_20161207_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='add_teams',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
