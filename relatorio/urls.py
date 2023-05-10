from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lista_sistema', views.lista_sistema, name='lista_sistema'),
    path('delete_sistema/<int:codigo>', views.delete_sistema, name='delete_sistema'),
    path('sistema_novo/', views.sistema_novo, name='sistema_novo'),
    path('create_sistema', views.create_sistema, name='create_sistema'),
    path('update_sistema/<int:codigo>/', views.update_sistema, name='update_sistema'),
    path('lista_carteira', views.lista_carteira, name='lista_carteira'),
    path('delete_carteira/<int:cod_carteira>', views.delete_carteira, name='delete_carteira'),
    path('carteira_nova/', views.carteira_nova, name='carteira_nova'),
    path('create_carteira', views.create_carteira, name='create_carteira'),
    path('update_carteira/<int:cod_carteira>/', views.update_carteira, name='update_carteira'),
    path('lista_classificacao', views.lista_classificacao, name='lista_classificacao'),
    path('classificacao_nova/', views.classificacao_nova, name='classificacao_nova'),
    path('update_classificacao/<int:id>/', views.update_classificacao, name='update_classificacao'),
    path('create_classificacao', views.create_classificacao, name='create_classificacao'),
    path('lista_ocorrencia', views.lista_ocorrencia, name='lista_ocorrencia'),
    path('ocorrencia_nova/', views.ocorrencia_nova, name='ocorrencia_nova'),
    path('delete_ocorrencia/<int:pk_interna>', views.delete_ocorrencia, name='delete_ocorrencia'),
    path('delete_classificacao/<int:id>', views.delete_classificacao, name='delete_classificacao'),
    path('create_ocorrencia', views.create_ocorrencia, name='create_ocorrencia'),
    path('update_ocorrencia/<int:pk_interna>/', views.update_ocorrencia, name='update_ocorrencia'),
]
