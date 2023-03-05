from django.db import models


class Historia(models.Model):
    id = models.AutoField(primary_key=True)
    oximetria = models.FloatField('Oximetria', max_length=5)
    f_respiratoria = models.FloatField('Frecuencia respiratoria', max_length=5)
    f_cardiaca = models.FloatField('Frecuencia cardiaca', max_length=5)
    temperatura = models.FloatField('Temperatura', max_length=5)
    p_arterial = models.FloatField('Presion arterial', max_length=5)
    glicemias = models.FloatField('Glicemias', max_length=5)
    diagnostico = models.CharField('Diagnostico', max_length=500)
    cuidados = models.CharField('Cuidados', max_length=500)
    fecha_reporte = models.DateTimeField()
    fecha_analisis_medico = models.DateField()
