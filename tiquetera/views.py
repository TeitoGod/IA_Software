from django.shortcuts import render
from django.http import JsonResponse
from .models import *
# Create your views here.

def index(request):
    return JsonResponse({'message': 'Hello World!'})

def create_user(req):
    if req.method != 'POST':
        return JsonResponse(
            {
                "data": "Null",
                "status": 404,
                "message": "Method Not Allowed"
            }
        )
    try:

        new_user = User(nombre_user=req.POST['nombre_user'])
        new_user.save()
        return JsonResponse(
            {
                "data": "nombre added",
                "status": 200,
                "message": "User created successfully"
            }
        )
    except Exception as e:
        print(e)
        return JsonResponse(
            {
                "data": "Null",
                "status": 400,
                "message": "Data incorrect, try again"
            }
        )




def create_reserva(req):
    if req.method == 'POST':

        return JsonResponse({'message': 'Hello World!'})