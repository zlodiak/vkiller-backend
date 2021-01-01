from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

from .models import User

def users(request):
    users = User.objects.all()   
    users_serialized = serializers.serialize('json', users)
    return JsonResponse(users_serialized, safe=False)

@csrf_exempt 
def login(request):
    isLogged = 'False'
    if request.method == 'POST':
        print('---', request.method)
        result = request.body.decode("utf-8")
        # login = json.loads(result).get('login')
        # print('=====', login)

    return JsonResponse({'isLogged': isLogged})