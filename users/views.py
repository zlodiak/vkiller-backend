from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
import json

from .models import User

def users(request):
    print(12333)
    users = User.objects.all()   
    users_serialized = serializers.serialize('json', users)
    return JsonResponse(users_serialized, safe=False)   