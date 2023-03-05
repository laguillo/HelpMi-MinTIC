from rest_framework import serializers
from Backend.models.medico import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Medico
        fields = ['id', 'usuario', 'especialidad']
        



