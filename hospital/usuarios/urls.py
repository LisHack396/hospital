from django.urls import path
from .views import *

urlpatterns = [
    path('Hospital/Registro', RegisterView.as_view(), name='registro'),
    path('Hospital/Login', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]