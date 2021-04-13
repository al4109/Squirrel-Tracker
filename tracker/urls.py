from django.urls import path

from . import views

urlpatterns = [
        path('map/',views.map),
        path('sightings/stats',views.stats_sighting),
        path('sightings/',views.all_sighting),
        path('sightings/add',views.create_sighting,name='create_sighting'),
        path('sightings/<unique_squirrel_id>',views.update_sighting,name='edit_sighting'),
]
