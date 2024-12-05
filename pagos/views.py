from django.shortcuts import render
from .logic import pagos_logic as vl
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def pagos_view(request, usuario=None):
    if request.method == 'GET':
        if usuario:
            pagos = vl.get_pagos_by_usuario(usuario)
            if pagos.exists():
                pagos_json = serializers.serialize('json', pagos)
                return HttpResponse(pagos_json, content_type='application/json')
            else:
                return JsonResponse({'error': 'No se encontraron pagos para este usuario'}, status=404)
        else:
            return JsonResponse({'error': 'El parámetro usuario es requerido'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)