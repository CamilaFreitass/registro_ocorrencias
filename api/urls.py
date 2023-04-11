from django.urls import path
from . import views
from .views import lista_classificacao, lista_sistema, lista_ocorrencia

urlpatterns = [
    path('lista_classificacao', lista_classificacao, name='lista_classificacao'),
    path('lista_sistema', lista_sistema, name='lista_sistema'),
    path('lista_carteira', views.lista_carteira, name='lista_carteira'),
    path('lista_ocorrencia', lista_ocorrencia, name='lista_ocorrencia'),
]