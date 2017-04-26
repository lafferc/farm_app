# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0004_tournament_add_matches'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournament',
            options={'permissions': (('csv_upload', 'Can add matches via CSV upload file'),)},
        ),
        migrations.AlterField(
            model_name='team',
            name='code',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([('code', 'sport')]),
        ),
    ]
