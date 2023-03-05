from rest_framework import serializers
from Backend.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'rol', 'nombre',
                  'apellido', 'documento', 'tipoDocumento', 'email', 'celular', 'direccion', 'genero']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'rol': user.rol,
            'documento': user.documento,
            'tipoDocumento': user.tipoDocumento,
            'email': user.email,
            'celular': user.celular,
            'direccion': user.direccion,
            'genero': user.genero
        }
