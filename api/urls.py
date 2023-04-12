from django.urls import path
from . import views
from .views import lista_classificacao, lista_sistema, lista_ocorrencia, delete_ocorrencia, delete_sistema
from .views import delete_classificacao, delete_carteira
urlpatterns = [
    path('lista_classificacao', lista_classificacao, name='lista_classificacao'),
    path('lista_sistema', lista_sistema, name='lista_sistema'),
    path('lista_carteira', views.lista_carteira, name='lista_carteira'),
    path('lista_ocorrencia', lista_ocorrencia, name='lista_ocorrencia'),
    path('delete_ocorrencia/<int:num_ocorrencia>/', delete_ocorrencia, name='delete_ocorrencia'),
    path('delete_sistema/<int:codigo>/', delete_sistema, name='delete_sistema'),
    path('delete_classificacao/<int:id>/', delete_classificacao, name='delete_classificacao'),
    path('delete_carteira/<int:cod_carteira>/', delete_carteira, name='delete_carteira'),
]