from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
import logging
import csv
import os

g_logger = logging.getLogger(__name__)


class Sport(models.Model):
    name = models.CharField(max_length=50, unique=True)
    add_teams = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=3, unique=True)
    sport = models.ForeignKey(Sport)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=200, unique=True)
    participants = models.ManyToManyField(User, through="Participant")
    sport = models.ForeignKey(Sport)
    bonus = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, default=2)
    late_get_bonus = models.BooleanField(default=True)
    state = models.IntegerField(default=1, choices=((0, "Pending"), (1, "Active"), (2, "finished")))
    winner = models.ForeignKey("Participant", null=True, blank=True, related_name='+')
    add_matches = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

    def update_table(self):
        g_logger.info("update_table")
        for participant in Participant.objects.filter(tournament=self):
            score = 0
            for prediction in Prediction.objects.filter(user=participant.user).filter(match__tournament=self):
                if prediction.score is not None:
                    score += prediction.score
            participant.score = score
            participant.save()

    def find_team(self, name):
        try:
            return Team.objects.get(sport=self.sport, name=name)
        except Team.DoesNotExist:
            return Team.objects.get(sport=self.sport, code=name)

class Participant(models.Model):
    tournament = models.ForeignKey(Tournament)
    user = models.ForeignKey(User)
    score = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2);

    def __str__(self):
        return "%s" % self.user

    class Meta:
        unique_together = ('tournament', 'user',)


class Match(models.Model):
    tournament = models.ForeignKey(Tournament)
    match_id = models.IntegerField()
    kick_off = models.DateTimeField()
    home_team = models.ForeignKey(Team, related_name='match_home_team')
    away_team = models.ForeignKey(Team, related_name='match_away_team')
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s V %s' % (self.home_team.code, self.away_team.code)

    def check_predictions(self):
        for user in self.tournament.participants.all():
            try:
                prediction = Prediction.objects.get(user=user, match=self)
            except Prediction.DoesNotExist:
                print("%s did not predict %s" % (user, match))
                prediction = Prediction(user=user, match=self, late=True)
            prediction.calc_score(self.score)
            prediction.save()

    class Meta:
        unique_together = ('tournament', 'match_id',)


class Prediction(models.Model):
    entered = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    match = models.ForeignKey(Match)
    prediction = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    score = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2);
    late = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return "%s: %s" % (self.user, self.match)

    def calc_score(self, result):
        if self.prediction == result:
            self.score = -self.bonus()
        elif (self.prediction < 0 and result < 0) or (self.prediction > 0 and result > 0):
            self.score = abs(result - self.prediction) - self.bonus()
        else:
            self.score = abs(result - self.prediction)

    def bonus(self):
        if self.late and not self.match.tournament.late_get_bonus:
            return 0
        return self.match.tournament.bonus

    class Meta:
        unique_together = ('user', 'match',)


@receiver(post_save, sender=Participant, dispatch_uid="add_draw_for_matches_already_played")
def add_draws(sender, instance, created, **kwargs):
    if created:
        g_logger.info("add_draw for %s", instance)
        for match in Match.objects.filter(tournament=instance.tournament, kick_off__lt=timezone.now()):
            try:
                with transaction.atomic():
                    Prediction(user=instance.user, match=match, late=True).save()
            except IntegrityError:
                g_logger.exception("User(%s) has already predicted %s" % (instance.user, match))


@receiver(post_save, sender=Match, dispatch_uid="cal_results_for_match")
def update_scores(sender, instance, created, **kwargs):
    if not created and instance.score is not None:
        g_logger.info("update_scores for %s", instance)
        instance.check_predictions()
        instance.tournament.update_table()

@receiver(post_save, sender=Sport, dispatch_uid="handle_teams_csv_upload")
def handle_team_upload(sender, instance, created, **kwargs):
    if not instance.add_teams:
        return
    g_logger.info("handle_teams_upload for %s csv:%s" % (instance, instance.add_teams))
    reader = csv.reader(instance.add_teams, delimiter=',')
    for row in reader:
        try:
            with transaction.atomic():
               Team(sport=instance, name=row[0], code=row[1]).save()
        except IntegrityError:
            g_logger.exception("Failed to add team")
    os.remove(instance.add_teams.name)
    instance.add_teams = None
    instance.save()

@receiver(post_save, sender=Tournament, dispatch_uid="handle_matches_csv_upload")
def handle_match_upload(sender, instance, created, **kwargs):
    if not instance.add_matches:
        return
    g_logger.info("handle_match_upload for %s csv:%s" % (instance, instance.add_matches))
    reader = csv.reader(instance.add_matches, delimiter=',')
    for row in reader:
        print row
        try:
            with transaction.atomic():
                Match(tournament=instance,
                      match_id=row[0],
                      home_team=instance.find_team(row[1]),
                      away_team=instance.find_team(row[2]),
                      kick_off=row[3]).save()
        except (IntegrityError, ValidationError, Team.DoesNotExist):
            g_logger.exception("Failed to add match")
    os.remove(instance.add_matches.name)
    instance.add_matches = None
    instance.save()