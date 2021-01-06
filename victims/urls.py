from django.urls import path
from . import views

urlpatterns = [
    path('victims', views.victims, name='victims'),
    path('victim', views.victim, name='victim'),
    path('victim_toggle_status', views.victim_toggle_status, name='victim_toggle_status'),
]