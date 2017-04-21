from django.http import JsonResponse
from rest_framework.views import APIView
from django.db.models import Count, Value, F, Sum
from django.utils.text import slugify
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from .decorators import islogged
from usuario.models import Usuario
from django.contrib.sessions.models import Session
from importlib import import_module
from django.conf import settings

SessionStore = import_module(settings.SESSION_ENGINE).SessionStore


class Authentication(APIView):
    def post(self, request):
        usuario = request.data['usuario']
        clave = request.data['clave']
        try:
            user = Usuario.objects.get(usuario=usuario, clave=clave)
        except Usuario.DoesNotExist:
            user = None

        if user is not None:
            s = SessionStore()
            s['id_usuario'] = user.id
            s.create()
            return JsonResponse({'estado': True, 'key': s.session_key})

        return JsonResponse({'estado': False, 'key': 'invalid'})


class Logout(APIView):
    def post(self, request):
        key = request.META['HTTP_AUTHORIZATION']
        try:
            session = Session.objects.get(pk=key)
        except Session.DoesNotExist:
            session = None

        if session is not None:
            session.delete()

        return JsonResponse({'message': 'Session borrada', 'estado': True})


class ModulosProyecto(APIView):
    def get(self, request):
        pass
