from django.db import models

from .familiar import Familiar
from .enfermero import Enfermero
from .historiaClinica import Historia
from .medico import Medico
from .user import User


class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    familiar = models.ForeignKey(Familiar, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE)
    enfermero = models.ForeignKey(Enfermero, on_delete=models.CASCADE)