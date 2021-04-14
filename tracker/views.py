from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from .models import SquirrelTracker
from .forms import Form, CreateForm
from django.db.models import Count

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

def stats(request):
    if request.method == 'GET':
        context = {
            'Squirrels': SquirrelTracker.objects.all(),
            'Squirrel_count': SquirrelTracker.objects.all().Count(),
            'Age_Adult_count':SquirrelTracker.objects.filter(Age = "Adult").Count(),    'Age_Juvenile_count':SquirrelTracker.objects.filter(Age = "Juvenile").Count(),
            'Shift_AM_count':SquirrelTracker.objects.filter(Shift = "AM").Count(),
            'Shift_PM_count':SquirrelTracker.objects.filter(Shift = "PM").Count(),
            'Color_Gray_count':SquirrelTracker.objects.filter(Primary_Fur_Color = "Gray").Count(),
            'Color_Cinnamon_count':SquirrelTracker.objects.filter(Primary_Fur_Color = "Cinnamon").Count(),
            'Color_Black_count':SquirrelTracker.objects.filter(Primary_Fur_Color = "Black").Count(),
            'Running_count':SquirrelTracker.objects.filter(Running = "True").Count(),
            'Chasing_count':SquirrelTracker.objects.filter(Chasing = "True").Count(),
            'Climbing_count':SquirrelTracker.objects.filter(Climbing = "True").Count(),
            'Eating_count':SquirrelTracker.objects.filter(Eating = "True").Count(),
            'Foraging_count':SquirrelTracker.objects.filter(Foraging = "True").Count(),
            }
        return render(request, 'tracker/stats.html', context)

def add(request):
    if request.method =='POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/')
    else:
        form = CreateForm()
        context = {
            'form':form,
            }
        return render(request,'tracker/add.html',context)
            

def detail(request, Unique_Squirrel_ID):
    squirrel= SquirrelTracker.objects.get( pk=Unique_Squirrel_ID)
    if request.method =='POST':
        form = CreateForm(request.POST, instance= squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/')
    else:
        form = CreateForm(instance = squirrel)
        context = {
            'form':form,
            'squirrel':squirrel,
            }
    return render(request,'tracker/edit.html',context)
