from django.shortcuts import render 
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def index(request):
    template = loader.get_template('home.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
