from django.contrib import admin

# Register your models here.
from pacientes.models import Paciente

admin.site.register(Paciente)