from rest_framework import serializers
from Backend.models.paciente import Paciente
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido']
