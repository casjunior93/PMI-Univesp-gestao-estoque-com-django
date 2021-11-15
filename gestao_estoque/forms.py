from django import forms
from django.forms import fields
from .models import Materiais, Movimentacao

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materiais
        fields = '__all__'

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ('id_pessoa', 'id_lote', 'id_material', 'quantidade', 'localizacao')
