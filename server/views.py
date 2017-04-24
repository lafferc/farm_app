from django.shortcuts import render 
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from competition.models import Tournament

@login_required
def index(request):
    template = loader.get_template('home.html')
    context = {
        'live_tournaments': Tournament.objects.filter(state=1),
        'closed_tournaments': Tournament.objects.filter(state=2),
    }
    return HttpResponse(template.render(context, request))
