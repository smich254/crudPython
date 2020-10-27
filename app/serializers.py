from .models import Correo
from rest_framework import serializers
class CorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = ('correo',)
