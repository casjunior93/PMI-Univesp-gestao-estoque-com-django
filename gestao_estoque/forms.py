from django import forms
from django.forms import fields
from .models import Materiais, Movimentacao, Pessoas

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materiais
        fields = '__all__'

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Pessoas
        fields = '__all__'

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = '__all__'

class MaterialUpdateForm(forms.ModelForm):
    class Meta:
        model = Materiais
        fields = '__all__'
