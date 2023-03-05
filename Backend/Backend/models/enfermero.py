from django.db import models
from .user import User

class Enfermero(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=500)
    auxiliar = models.BooleanField(default=False)
