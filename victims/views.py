from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Victim

def victims(request):
    victims = Victim.objects.all()   
    victims_serialized = serializers.serialize('json', victims)
    return JsonResponse(victims_serialized, safe=False)
