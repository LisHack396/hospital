from django.db import models
from django.utils.translation import gettext_lazy as _

class Paciente(models.Model):
    class Tratamiento(models.TextChoices):
        medico = "Medico", _("Medico")
        alta = "Alta", _("Alta")
        estudio = "Estudio", _("Estudio")
        quirurgico = "Quirurgico", _("Quirurgico")
        urgencia = "Urgencia", _("Urgencia")
    class Sexo(models.TextChoices):
        masculino = "M", _("M")
        femenino = "F", _("F")
        otro = "Otro", _("Otro")
    historia = models.CharField(max_length=6, unique=True)
    ci = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10, choices=Sexo)
    direccion = models.CharField(max_length=60, blank=True)
    area_de_salud = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=255, blank=True, null=True)
    #tratamiento = models.CharField(max_length=25, choices=Tratamiento, default=Tratamiento.medico)

    class Meta:
        db_table = 'Paciente'
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'
        ordering = ['historia']
        permissions = (("es_secretaria", "Puede administrar"),)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
