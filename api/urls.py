from django.urls import path
from . import views
from .views import lista_classificacao, lista_sistema, lista_ocorrencia, delete_ocorrencia, delete_sistema
from .views import delete_classificacao, delete_carteira, create_ocorrencia, update_ocorrencia, create_sistema
from .views import update_sistema, update_carteira, create_carteira, update_classificacao, create_classificacao
app_name = 'api'

urlpatterns = [
    path('lista_classificacao', lista_classificacao, name='lista_classificacao'),
    path('delete_classificacao/<int:id>/', delete_classificacao, name='delete_classificacao'),
    path('update_classificacao/<int:id>/', update_classificacao, name='update_classificacao'),
    path('create_classificacao/', create_classificacao, name='create_classificacao'),
    path('lista_sistema', lista_sistema, name='lista_sistema'),
    path('delete_sistema/<int:codigo>/', delete_sistema, name='delete_sistema'),
    path('create_sistema/', create_sistema, name='create_sistema'),
    path('update_sistema/<int:codigo>/', update_sistema, name='update_sistema'),
    path('lista_carteira', views.lista_carteira, name='lista_carteira'),
    path('create_carteira/', create_carteira, name='create_carteira'),
    path('update_carteira/<int:cod_carteira>/', update_carteira, name='update_carteira'),
    path('delete_carteira/<int:cod_carteira>/', delete_carteira, name='delete_carteira'),
    path('lista_ocorrencia', lista_ocorrencia, name='lista_ocorrencia'),
    path('delete_ocorrencia/<int:pk_interna>/', delete_ocorrencia, name='delete_ocorrencia'),
    path('create_ocorrencia/', create_ocorrencia, name='create_ocorrencia'),
    path('update_ocorrencia/<int:pk_interna>/', update_ocorrencia, name='update_ocorrencia'),
]