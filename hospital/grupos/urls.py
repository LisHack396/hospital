from django.urls import path
from . import views

urlpatterns = [
    path('Hospital/grupos/', views.ListarGrupos.as_view(), name='grupos_lista'),
    path('Hospital/grupos/crear/', views.CrearGrupo.as_view(), name='crear_grupo'),
    path('Hospital/grupos/actualizar/<int:pk>', views.ModificarGrupo.as_view(), name='actualizar_grupo'),
    path('Hospital/grupos/eliminar/<int:pk>', views.EliminarGrupo.as_view(), name='eliminar_grupo')
]