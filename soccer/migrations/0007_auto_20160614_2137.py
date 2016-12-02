# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0006_auto_20160614_2126'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together=set([('tournament', 'user')]),
        ),
    ]
