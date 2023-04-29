from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms, name='forms'),
    path('processa_formulario/', views.processa_formulario, name="processa_formulario"),
    path('lista_sistema', views.lista_sistema, name='lista_sistema'),
    path('sist_novo/', views.sist_novo, name='sist_novo'),
    path('processa_sist/', views.processa_sist, name="processa_sist"),
    path('update_sist/<int:codigo>', views.update_sist, name='update_sist'),
    path('editar_sist/<int:codigo>', views.editar_sist, name='editar_sist'),
    path('lista_carteira', views.lista_carteira, name='lista_carteira'),
    path('carteira_nova/', views.carteira_nova, name='carteira_nova'),
    path('processa_carteira/', views.processa_carteira, name="processa_carteira"),
    path('update_carteira/<int:cod_carteira>', views.update_carteira, name='update_carteira'),
    path('editar_carteira/<int:cod_carteira>', views.editar_carteira, name='editar_carteira'),
    path('lista_classificacao', views.lista_classificacao, name='lista_classificacao'),
    path('lista_ocorrencia', views.lista_ocorrencia, name='lista_ocorrencia'),
    path('ocorrencia_nova/', views.ocorrencia_nova, name='ocorrencia_nova'),
    path('delete_ocorrencia/<int:num_ocorrencia>', views.delete_ocorrencia, name='delete_ocorrencia'),
    path('delete_sistema/<int:codigo>', views.delete_sistema, name='delete_sistema'),
    path('delete_classificacao/<int:id>', views.delete_classificacao, name='delete_classificacao'),
    path('delete_carteira/<int:cod_carteira>', views.delete_carteira, name='delete_carteira'),
    path('create_ocorrencia', views.create_ocorrencia, name='create_ocorrencia'),
    path('update_ocorrencia/<int:num_ocorrencia>/', views.update_ocorrencia, name='update_ocorrencia'),

]
