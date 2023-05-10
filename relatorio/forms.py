from django import forms
from .models import Ocorrencia, Sistema, Carteira, DiscadorOcorrencia

class OcorrenciaForms(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['num_ocorrencia', 'desc_ocorrencia']


class SistemaForms(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = ['nome_sistema']


class CarteiraForms(forms.ModelForm):
    class Meta:
        model = Carteira
        fields = ['nome_carteira']


class DiscadorOcorrenciaForms(forms.ModelForm):
    class Meta:
        model = DiscadorOcorrencia
        fields = ['sist', 'carteira', 'ocorrencia', 'alo', 'cpc', 'promessa']

