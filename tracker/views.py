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
            SquirrelTracker.objects.filter(Age ='Adult').aggregate(Adult_Squirrels = Count('Unique_Squirrel_ID')),
            SquirrelTracker.objects.filter(Primary Fur Color ='Cinnamon').aggregate(Cinnamon_Color_Squirrels = Count('Unique_Squirrel_ID')),
            SquirrelTracker.objects.filter(Location ='Above Ground').aggregate(Found_Above_Ground_Squirrels = Count('Unique_Squirrel_ID')),
            SquirrelTracker.objects.filter(Shift ='AM').aggregate(Sightings_Occured_Morning = Count('Unique_Squirrel_ID')),
            SquirrelTracker.objects.filter(Date ='10062018').aggregate(Sightings_Occured_October6th_2018 = Count('Unique_Squirrel_ID')),
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
    
def edit_sighting(request, Unique_Squirrel_ID):
    squirrel= get_object_or_404(SquirrelTracker, pk = Unique_Squirrel_ID)
    if request.method =='POST':
        try:
            form = Form(request.POST, instance= squirrel)
			form.save()
			return redirect(f'/traker/sightings/')
		except (KeyError, SquirrelTracker.DoesNotExist):
			return render(request, 'tracker/edit.html', {
			'squirrel': squirrel,
            'error_message': "There is no such Squirrel.",})
    else:
		try:
        	form = Form(instance = squirrel)
        	context = {
            'form':form,
            'squirrel':squirrel,
            }
			return render(request,'tracker/edit.html',context)
		except (KeyError, SquirrelTracker.DoesNotExist):
			return render(request, 'tracker/edit.html', {
			'squirrel': squirrel,
            'error_message': "There is no such Squirrel.",})
  
    
