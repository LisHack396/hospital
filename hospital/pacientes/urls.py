from django.urls import path
from . import views

urlpatterns = [
    path('Hospital/pacientes/', views.ListarPacientes.as_view(), name='pacientes_lista'),
    path('Hospital/pacientes/insertar/', views.CrearPaciente.as_view(), name='crear_paciente'),
    path('Hospital/pacientes/actualizar/<int:pk>', views.ModificarPaciente.as_view(), name='actualizar_paciente'),
    path('Hospital/pacientes/eliminar/<int:pk>', views.EliminarPaciente.as_view(), name='eliminar_paciente')
]