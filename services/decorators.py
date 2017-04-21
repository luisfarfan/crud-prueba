import requests
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from django.http import JsonResponse


def islogged(func):
    def wrapper(*args, **kwargs):
        request = args[0]
        key = request.META['HTTP_AUTHORIZATION']
        islogueado = Session.objects.filter(pk=key).count()
        if islogueado == 0:
            return JsonResponse(status=404, data={'status': 'false', 'message': 'Key invalido, permiso denegado'})
        return func(*args, **kwargs)

    return wrapper
