from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sist_novo/', views.sist_novo, name='sist_novo'),
    path('forms/', views.forms, name='forms'),
    path('processa_sist/', views.processa_sist, name="processa_sist"),
    path('processa_formulario/', views.processa_formulario, name="processa_formulario"),
    path('deletar/<int:id>', views.deletar, name="deletar"),
    path('lista_sist',views.lista_sist, name='lista_sist'),
    path('buscar', views.buscar, name='buscar'),
]
