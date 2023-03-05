from django.contrib import admin

from Backend.models.historiaClinica import Historia
from Backend.models.familiar import Familiar
from Backend.models.user import User
from Backend.models.medico import Medico
from Backend.models.paciente import Paciente

# Register your models here.
admin.site.register(User)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Historia)
admin.site.register(Familiar)
