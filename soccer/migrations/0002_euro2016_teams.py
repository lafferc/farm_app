# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

teams = [("Albania", "ALB"),
         ("Austria", "AUT"),
         ("Belgium", "BEL"),
         ("Croatia", "CRO"),
         ("Czech Republic", "CZE"),
         ("England", "ENG"),
         ("France", "FRA"),
         ("Germany", "GER"),
         ("Hungary", "HUN"),
         ("Iceland", "ISL"),
         ("Italy", "ITA"),
         ("Northern Ireland", "NIR"),
         ("Poland", "POL"),
         ("Portugal", "POR"),
         ("Republic of Ireland", "IRL"),
         ("Romania", "ROU"),
         ("Russia", "RUS"),
         ("Slovakia", "SVK"),
         ("Spain", "ESP"),
         ("Sweden", "SWE"),
         ("Switzerland", "SUI"),
         ("Turkey", "TUR"),
         ("Ukraine", "UKR"),
         ("Wales", "WAL")]

def add_euro2016_teams(apps, schema_editor):
    Team = apps.get_model("soccer", "Team")
    for name, code in teams:
        Team(name=name, code=code).save()


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_euro2016_teams)
    ]
