from django.contrib import admin
from soccer.models import Team, Tournament, Match, Prediction, Participant, update_table


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 0
    readonly_fields = ('score',)

    def has_delete_permission(self, request, obj=None):
        return False


def pop_leaderboard(modeladmin, request, queryset):
    for tournament in queryset:
        update_table(tournament)


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
            print("adding %s to list" % match.tournament)
            tourns.append(match.tournament)
        for user in match.tournament.participants.all():
            try:
                prediction = Prediction.objects.get(user=user, match=match)
            except Prediction.DoesNotExist:
                print("%s did not predict %s" % (user, match))
                prediction = Prediction(user=user, match=match)
            prediction.calc_score(match.score)
            prediction.save()
    for tourn in tourns:
        update_table(tourn)

class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_id', 'home_team', 'away_team', 'kick_off', 'score')
    actions = [calc_match_result]


class PredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'match', 'entered')
    readonly_fields = ('score',)

    list_filter = ('match','user')


admin.site.register(Team, TeamAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Prediction, PredictionAdmin)
