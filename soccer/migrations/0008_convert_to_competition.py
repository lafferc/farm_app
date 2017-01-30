# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def convert_to_competition(apps, schema_editor):
    Sport = apps.get_model("competition", "Sport") 
    Team = apps.get_model("competition", "Team")
    SoccerTeam = apps.get_model("soccer", "Team")
    Tournament = apps.get_model("competition", "Tournament")
    SoccerTournament = apps.get_model("soccer", "Tournament")
    Participant = apps.get_model("competition", "Participant")
    SoccerParticipant = apps.get_model("soccer", "Participant")
    Match = apps.get_model("competition", "Match")
    SoccerMatch = apps.get_model("soccer", "Match")
    Prediction = apps.get_model("competition", "Prediction")
    SoccerPrediction = apps.get_model("soccer", "Prediction")

    soccer = Sport(name="soccer")
    soccer.save()

    teams = {}
    for team in SoccerTeam.objects.all():
        teams[team.pk] = Team(name=team.name, code=team.code, sport=soccer)
        teams[team.pk].save()

    for tourn in SoccerTournament.objects.all():
        newTourn = Tournament(name=tourn.name, sport=soccer)
        newTourn.save()

        for par in SoccerParticipant.objects.filter(tournament=tourn):
            Participant(tournament=newTourn, user=par.user, score=par.score).save()

        for match in SoccerMatch.objects.filter(tournament=tourn):
            newMatch = Match(tournament=newTourn, match_id=match.match_id, kick_off=match.kick_off, 
                             home_team=teams[match.home_team.pk], away_team=teams[match.away_team.pk],
                             score=match.score)
            newMatch.save()

            for pred in SoccerPrediction.objects.filter(match=match):
                Prediction(entered=pred.entered, user=pred.user, match=newMatch,
                           prediction=pred.prediction, score=pred.score).save()


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0007_auto_20160614_2137'),
        ('competition', '0004_tournament_add_matches'),
    ]

    operations = [
        migrations.RunPython(convert_to_competition)
    ]
