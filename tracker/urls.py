from django.urls import path

from . import views

app_name = 'sightings'

urlpatterns = [
        path('', views.index, name='index'),
        path('map/',views.show_map, name='map'),
        path('sightings/add/', views.add, name='add'),
        path('sightings/stats/', views.stats, name='stats'),
        path('sightings/<Unique_Squirrel_ID>/', views.detail, name='detail')
        ]
