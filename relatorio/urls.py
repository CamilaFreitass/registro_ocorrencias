from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms, name='forms'),
    path('processa_formulario/', views.processa_formulario, name="processa_formulario"),
    path('deletar/<int:id>', views.deletar, name="deletar"),
    path('lista_sist', views.lista_sist, name='lista_sist'),
    path('sist_novo/', views.sist_novo, name='sist_novo'),
    path('processa_sist/', views.processa_sist, name="processa_sist"),
    path('update_sist/<int:codigo>', views.update_sist, name='update_sist'),
    path('editar_sist/<int:codigo>', views.editar_sist, name='editar_sist'),
    path('deletar_sist/<int:codigo>', views.deletar_sist, name='deletar_sist'),
    path('lista_carteira', views.lista_carteira, name='lista_carteira'),
    path('carteira_nova/', views.carteira_nova, name='carteira_nova'),
    path('processa_carteira/', views.processa_carteira, name="processa_carteira"),
    path('deletar_carteira/<int:cod_carteira>', views.deletar_carteira, name='deletar_carteira'),
    path('update_carteira/<int:cod_carteira>', views.update_carteira, name='update_carteira'),
    path('editar_carteira/<int:cod_carteira>', views.editar_carteira, name='editar_carteira'),
    path('buscar', views.buscar, name='buscar'),
    path('lista_ocorrencia', views.lista_ocorrencia, name='lista_ocorrencia'),
    path('ocorrencia_nova/', views.ocorrencia_nova, name='ocorrencia_nova'),
    path('processa_ocorrencia/', views.processa_ocorrencia, name="processa_ocorrencia"),
]
