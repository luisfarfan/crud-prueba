from rest_framework import routers
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'authentication/$', Authentication.as_view()),
]
