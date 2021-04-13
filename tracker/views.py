from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import SquirrelTracker
from .forms import Form, CreateForm

# def index(request):
#     return render(request, 'tracker/index.html', {})

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

def all_sighting(request):
    
def stats_sighting(request):
    statdict = [
            SquirrelTracker.objects.filter(Age ='Adult').aggregate(Adult_Squirrels = Count('unique_squirrel_id')),
            SquirrelTracker.objects.filter(Primary Fur Color ='Cinnamon').aggregate(Cinnamon_Color_Squirrels = Count('unique_squirrel_id')),
            SquirrelTracker.objects.filter(Location ='Above Ground').aggregate(Found_Above_Ground_Squirrels = Count('unique_squirrel_id')),
            SquirrelTracker.objects.filter(Shift ='AM').aggregate(Sightings_Occured_Morning = Count('unique_squirrel_id')),
            SquirrelTracker.objects.filter(Date ='10062018').aggregate(Sightings_Occured_October6th_2018 = Count('unique_squirrel_id')),
            ]
    stat_list=[]
    for stat in statdict:
        stat_list.append([list(stat.keys())[0],list(stat.values())[0]])

    context = {'stats':sighting_list,}
    return render(request, 'tracker/stats.html', context)
    
def create_sighting(request):
    if request.method =='POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/traker/sightings/')
    else:
        form = CreateForm()
    context = {
            'form':form,
            }
    return render(request,'tracker/create.html',context)
    
def edit_sighting(request, unique_squirrel_id):
    squirrel= SquirrelTracker.objects.get_object_or_404(pk =unique_squirrel_id)
    if request.method =='POST':
        form = Form(request.POST, instance= squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/traker/sightings/')
    else:
        form = Form(instance = squirrel)
        context = {
            'form':form,
            'squirrel':squirrel,
            }
    return render(request,'tracker/edit.html',context)
    
