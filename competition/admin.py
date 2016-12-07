from django.contrib import admin
from competition.models import Team, Tournament, Match, Prediction, Participant
from competition.models import Sport
import logging

g_logger = logging.getLogger(__name__)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 0
    readonly_fields = ('score',)

    def has_delete_permission(self, request, obj=None):
        return False


def pop_leaderboard(modeladmin, request, queryset):
    g_logger.info("pop_leaderboard(%r, %r, %r", modeladmin, request, queryset)
    for tournament in queryset:
        tournament.update_table()


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = ( ParticipantInline, )
    actions = [pop_leaderboard]


def calc_match_result(modeladmin, request, queryset):
    tourns = []
    for match in queryset:
        if match.score is None:
            continue
        if match.tournament not in tourns:
            g_logger.info("adding %s to list" % match.tournament)
            tourns.append(match.tournament)
        match.check_predictions()
    for tourn in tourns:
        tourn.update_table()


class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_id', 'home_team', 'away_team', 'kick_off', 'score')
    actions = [calc_match_result]


class PredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'match', 'entered')
    readonly_fields = ('score', "late")

    list_filter = ('match','user')


admin.site.register(Sport)
admin.site.register(Team, TeamAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Prediction, PredictionAdmin)
