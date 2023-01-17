from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms, name='forms'),
    path('processa_formulario/', views.processa_formulario, name="processa_formulario"),
    path('listagem/', views.listagem, name="listagem"),
    path('deletar/<int:id>', views.deletar, name="deletar"),
    path('buscar', views.buscar, name='buscar')
]
