from rest_framework import serializers
from Backend.models.historiaClinica import Historia


class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['id', 'oximetria', 'f_respiratoria',
                  'f_cardiaca', 'temperatura', 'p_arterial', 'glicemias']
