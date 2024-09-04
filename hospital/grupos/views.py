from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Grupo
from .forms import GrupoForm

class ListarGrupos(ListView, LoginRequiredMixin):
    model = Grupo
    template_name = "grupos/lista.html"
    login_url = "/login/"
    redirect_field_name = "login"

class CrearGrupo(CreateView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Grupo
    form_class = GrupoForm
    permission_required = "catalog.es_secretaria"
    template_name = "grupos/crear.html"
    success_url = reverse_lazy("grupos_lista")
    login_url = "/login/"
    redirect_field_name = "login"

class ModificarGrupo(UpdateView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Grupo
    form_class = GrupoForm
    permission_required = "catalog.es_secretaria"
    template_name = "grupos/actualizar.html"
    success_url = reverse_lazy("grupos_lista")
    login_url = "/login/"
    redirect_field_name = "login"

class EliminarGrupo(DeleteView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Grupo
    permission_required = "catalog.es_secretaria"
    template_name = "grupos/eliminar.html"
    success_url = reverse_lazy("grupos_lista")
    login_url = "/login/"
    redirect_field_name = "login"