from django.http import HttpResponse
from django.shortcuts import render
from .models import SquirrelTracker
from .forms import Form, CreateForm

def index(request):
    return render(request, 'tracker/index.html', {})

def index(request):
    squirrels = SquirrelTracker.objects.all()
    context = {
        'squirrels': squirrels
    }
    return render(request, 'tracker/index.html', context)

def show_map(request):
    sightings = SquirrelTracker.objects.all()[:100]
    context = {
        'sightings': sightings
    }
    return render(request, 'tracker/map.html', context)

