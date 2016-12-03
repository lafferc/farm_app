# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DoseGiven',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('dose', models.ForeignKey(to='sheep.Dose')),
            ],
        ),
        migrations.CreateModel(
            name='LambingYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.DateField()),
                ('scanned', models.IntegerField()),
                ('born', models.IntegerField()),
                ('yenned', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sheep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('gender', models.CharField(max_length=50, choices=[(b'R', b'Ram'), (b'E', b'Ewe')])),
                ('yob', models.DateField(null=True, blank=True)),
                ('age', models.CharField(max_length=50, choices=[(b'S', b'sheep'), (b'H', b'hogget'), (b'L', b'lamb')])),
                ('is_alive', models.BooleanField(default=True)),
                ('comment', models.CharField(max_length=50, null=True, blank=True)),
                ('dossed', models.ManyToManyField(to='sheep.Dose', through='sheep.DoseGiven')),
                ('parent', models.ForeignKey(blank=True, to='sheep.Sheep', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('value', models.IntegerField()),
                ('sheep', models.ForeignKey(to='sheep.Sheep')),
            ],
        ),
        migrations.AddField(
            model_name='lambingyear',
            name='sheep',
            field=models.ForeignKey(to='sheep.Sheep'),
        ),
        migrations.AddField(
            model_name='dosegiven',
            name='sheep',
            field=models.ForeignKey(to='sheep.Sheep'),
        ),
    ]
