from django.db import models
from .user import User


class Familiar(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_paciente = models.CharField(max_length=(50))
