from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.verifica_atividade, name="index"),
    path('cadastro', views.cadastro, name="cadastro")
]