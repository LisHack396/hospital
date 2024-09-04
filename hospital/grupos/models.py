from django.db import models
from pacientes.models import Paciente

class Grupo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    cantidad_miembros = models.PositiveIntegerField()
    pacientes = models.ManyToManyField(Paciente, related_name='pacientes')
    class Meta:
        db_table = 'Grupo'
        ordering = ['nombre']
        db_table = 'Grupo_Pacientes'
        verbose_name = 'grupo_paciente'
        verbose_name_plural = 'grupo_pacientes'
        permissions = (('es_secretaria', 'Puede administrar'),)
    def __str__(self):
        return self.nombre
    def save(self, *args, **kwargs):
        miembros = Grupo.objects.filter(pacientes__id=self.id).count()
        if miembros <= self.cantidad_miembros:
            super(Grupo, self).save(*args, **kwargs)
