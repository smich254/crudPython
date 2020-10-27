from django.shortcuts import render
from .models import Correo
from .serializers import CorreoSerializer
from rest_framework import viewsets
# Create your views here.
class CorreoViewSet(viewsets.ModelViewSet):
   queryset = Correo.objects.all()
   serializer_class = CorreoSerializer