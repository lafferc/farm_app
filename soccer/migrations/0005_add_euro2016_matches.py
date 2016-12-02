# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

euro2016 = { 'euro2016' : [
    (1, "France", "Romania", "2016-06-10 19:00:00"),
    (2, "Albania", "Switzerland", "2016-06-11 13:00:00"),
    (3, "Wales", "Slovakia", "2016-06-11 16:00:00"),
    (4, "England", "Russia", "2016-06-11 19:00:00"),
    (5, "Turkey", "Croatia", "2016-06-12 13:00:00"),
    (6, "Poland", "Northern Ireland", "2016-06-12 16:00:00"),
    (7, "Germany", "Ukraine", "2016-06-12 19:00:00"),
    (8, "Spain", "Czech Republic", "2016-06-13 13:00:00"),
    (9, "Republic of Ireland", "Sweden", "2016-06-13 16:00:00"),
    (10, "Belgium", "Italy", "2016-06-13 19:00:00"),
    (11, "Austria", "Hungary", "2016-06-14 16:00:00"),
    (12, "Portugal", "Iceland", "2016-06-14 19:00:00"),
    (13, "Russia", "Slovakia", "2016-06-15 13:00:00"),
    (14, "Romania", "Switzerland", "2016-06-15 16:00:00"),
    (15, "France", "Albania", "2016-06-15 19:00:00"),
    (16, "England", "Wales", "2016-06-16 13:00:00"),
    (17, "Ukraine", "Northern Ireland", "2016-06-16 16:00:00"),
    (18, "Germany", "Poland", "2016-06-16 19:00:00"),
    (19, "Italy", "Sweden", "2016-06-17 13:00:00"),
    (20, "Czech Republic", "Croatia", "2016-06-17 16:00:00"),
    (21, "Spain", "Turkey", "2016-06-17 19:00:00"),
    (22, "Belgium", "Republic of Ireland", "2016-06-18 13:00:00"),
    (23, "Iceland", "Hungary", "2016-06-18 16:00:00"),
    (24, "Portugal", "Austria", "2016-06-18 19:00:00"),
    (25, "Romania", "Albania", "2016-06-19 19:00:00"),
    (26, "Switzerland", "France", "2016-06-19 19:00:00"),
    (27, "Russia", "Wales", "2016-06-20 19:00:00"),
    (28, "Slovakia", "England", "2016-06-20 19:00:00"),
    (29, "Ukraine", "Poland", "2016-06-21 16:00:00"),
    (30, "Northern Ireland", "Germany", "2016-06-21 16:00:00"),
    (31, "Czech Republic", "Turkey", "2016-06-21 19:00:00"),
    (32, "Croatia", "Spain", "2016-06-21 19:00:00"),
    (33, "Iceland", "Austria", "2016-06-22 16:00:00"),
    (34, "Hungary", "Portugal", "2016-06-22 16:00:00"),
    (35, "Italy", "Republic of Ireland", "2016-06-22 19:00:00"),
    (36, "Sweden", "Belgium", "2016-06-22 19:00:00"),
]}

def add_euro2016_fixtures(apps, schema_editor):
    Tournament = apps.get_model("soccer", "Tournament")
    Match = apps.get_model("soccer", "Match")
    Team = apps.get_model("soccer", "Team")

    team_lookup = {}
    for team in Team.objects.all():
        team_lookup[team.name] = team
    
    for t_name, matches in euro2016.iteritems():
        t = Tournament(name=t_name)
        t.save()

        for m_id, home, away, time in matches:
            Match(tournament=t, match_id=m_id, home_team=team_lookup[home],away_team=team_lookup[away], kick_off=time).save()


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0004_auto_20160611_1013'),
    ]

    operations = [
        migrations.RunPython(add_euro2016_fixtures)
    ]
