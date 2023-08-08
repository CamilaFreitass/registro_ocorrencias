from django import forms
from .models import Ocorrencia, Sistema, Carteira, DiscadorOcorrencia
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class OcorrenciaForms(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['num_ocorrencia', 'desc_ocorrencia']


class SistemaForms(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = ['nome_sistema']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper


class CarteiraForms(forms.ModelForm):
    class Meta:
        model = Carteira
        fields = ['nome_carteira']


class DiscadorOcorrenciaForms(forms.ModelForm):
    class Meta:
        model = DiscadorOcorrencia
        fields = ['sist', 'carteira', 'ocorrencia', 'alo', 'cpc', 'promessa']

