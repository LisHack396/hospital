from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Paciente
from .forms import PacienteForm

class ListarPacientes(ListView, LoginRequiredMixin):
    model = Paciente
    template_name = "pacientes/lista.html"
    login_url = "/login/"
    redirect_field_name = "login"

class CrearPaciente(CreateView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Paciente
    form_class = PacienteForm
    permission_required = "catalog.es_secretaria"
    template_name = "pacientes/crear.html"
    success_url = reverse_lazy("pacientes_lista")
    login_url = "/login/"
    redirect_field_name = "login"

class ModificarPaciente(UpdateView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Paciente
    form_class = PacienteForm
    permission_required = "catalog.es_secretaria"
    template_name = "pacientes/actualizar.html"
    success_url = reverse_lazy("pacientes_lista")
    login_url = "/login/"
    redirect_field_name = "login"

class EliminarPaciente(DeleteView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Paciente
    permission_required = "catalog.es_secretaria"
    template_name = "pacientes/eliminar.html"
    success_url = reverse_lazy("pacientes_lista")
    login_url = "/login/"
    redirect_field_name = "login"