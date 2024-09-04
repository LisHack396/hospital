from django.urls import path
from . import views

urlpatterns = [
    path('Hospital/diagnosticos/', views.ListarDiagnosticos.as_view(), name='diagnosticos_lista'),
    path('Hospital/diagnosticos/crear/', views.CrearDiagnostico.as_view(), name='crear_diagnostico'),
    path('Hospital/diagnosticos/actualizar/<int:pk>', views.ModificarDiagnostico.as_view(), name='actualizar_diagnostico'),
    path('Hospital/diagnosticos/eliminar/<int:pk>', views.EliminarDiagnostico.as_view(), name='eliminar_diagnostico')
]