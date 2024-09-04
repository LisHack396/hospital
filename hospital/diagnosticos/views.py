from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Diagnostico
from .forms import DiagnosticoForm

class ListarDiagnosticos(ListView, LoginRequiredMixin):
    model = Diagnostico
    template_name = "diagnosticos/lista.html"
    login_url = "/login/"
    redirect_field_name = "login"

class CrearDiagnostico(CreateView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Diagnostico
    form_class = DiagnosticoForm
    permission_required = "catalog.es_doctor"
    template_name = "diagnosticos/crear.html"
    success_url = reverse_lazy("diagnosticos_lista")
    login_url = "/login/"
    redirect_field_name = "login"

class ModificarDiagnostico(UpdateView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Diagnostico
    form_class = DiagnosticoForm
    permission_required = "catalog.es_doctor"
    template_name = "diagnosticos/actualizar.html"
    success_url = reverse_lazy("diagnosticos_lista")
    login_url = "/login/"
    redirect_field_name = "login"

class EliminarDiagnostico(DeleteView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Diagnostico
    permission_required = "catalog.es_doctor"
    template_name = "diagnosticos/eliminar.html"
    success_url = reverse_lazy("diagnosticos_lista")
    login_url = "/login/"
    redirect_field_name = "login"