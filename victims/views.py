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

# def victims(request):
#     print('=-=-=', request.GET)
#     # if request.method == 'GET':
        

#         # result = request.body.decode("utf-8")
#         # user_id = json.loads(result).get('user_id')
        
#         # victims = Victim.objects.filter(id_user=user_id) 

#     return JsonResponse({'isLogged': isLogged})
