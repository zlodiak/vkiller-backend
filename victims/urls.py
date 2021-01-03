from django.urls import path
from . import views

urlpatterns = [
    path('victims', views.victims, name='victims'),
]