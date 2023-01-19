from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms, name='forms'),
    path('processa_formulario/', views.processa_formulario, name="processa_formulario"),
    path('deletar/<int:id>', views.deletar, name="deletar"),
    path('buscar', views.buscar, name='buscar'),
    path('listagem2/', views.listagem2, name="listagem2")
]
