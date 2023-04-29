from django import forms
from .models import Ocorrencia

class OcorrenciaForms(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['num_ocorrencia', 'desc_ocorrencia']

