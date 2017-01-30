from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.db import IntegrityError, transaction


class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=200, unique=True)
    participants = models.ManyToManyField(User, through="Participant", related_name='soc_tournament_participants')

    def __str__(self):
        return self.name


class Participant(models.Model):
    tournament = models.ForeignKey(Tournament)
    user = models.ForeignKey(User, related_name='soc_participant_user')
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

    class Meta:
        unique_together = ('tournament', 'match_id',)


class Prediction(models.Model):
    entered = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='soc_prediction_user')
    match = models.ForeignKey(Match)
    prediction = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    score = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2);

    def __str__(self):
        return "%s: %s" % (self.user, self.match)

    def calc_score(self, result):
        if self.prediction == result:
            self.score = -2
        elif (self.prediction < 0 and result < 0) or (self.prediction > 0 and result > 0):
            self.score = abs(result - self.prediction) - 2
        else:
            self.score = abs(result - self.prediction)

    class Meta:
        unique_together = ('user', 'match',)


@receiver(post_save, sender=Participant, dispatch_uid="add_draw_for_matches_already_played")
def add_draws(sender, instance, created, **kwargs):
    if created:
        for match in Match.objects.filter(tournament=instance.tournament, kick_off__lt=timezone.now()):
            try:
                with transaction.atomic():
                    Prediction(user=instance.user, match=match).save()
            except IntegrityError:
                print("User(%s) has already predicted %s" % (instance.user, match))


def update_table(tournament):
    for participant in Participant.objects.filter(tournament=tournament):
        score = 0
        for prediction in Prediction.objects.filter(user=participant.user).filter(match__tournament=tournament):
            if prediction.score is not None:
                score += prediction.score
        participant.score = score
        participant.save()


@receiver(post_save, sender=Match, dispatch_uid="cal_results_for_match")
def add_draws(sender, instance, created, **kwargs):
    if not created and instance.score is not None:
        for user in instance.tournament.participants.all():
            try:
                prediction = Prediction.objects.get(user=user, match=instance)
            except Prediction.DoesNotExist:
                print("User (%s) did not predict %s" % (user, instance))
                prediction = Prediction(user=user, match=instance)
            prediction.calc_score(instance.score)
            prediction.save()
        update_table(instance.tournament)
