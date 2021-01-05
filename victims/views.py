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


@csrf_exempt
def victim(request):
    if request.method == 'POST':
        result = request.body.decode("utf-8")
        form_data = json.loads(result).get('formData')
        pk = json.loads(result).get('pk')

        Victim.objects.filter(pk=pk).update(firstname=form_data['firstname'], \
        lastname=form_data['lastname'], \
        gender=form_data['gender'], \
        is_complete=form_data['is_complete'], \
         address=form_data['address'])

    return JsonResponse({'response_code': 200})