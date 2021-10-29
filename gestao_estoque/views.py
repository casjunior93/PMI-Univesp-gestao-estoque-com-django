from django.shortcuts import render

# Create your views here.
from django.http import Http404
from .models import Materiais
from .models import Pessoas
from .models import Movimentacao


def home(request):
    return render(request,'home.html')

def materiais(request):
    materiais = Materiais.objects.all()
    return render(request, 'materiais.html', {
        'materiais': materiais
    })

def funcionarios(request):
    funcionarios = Pessoas.objects.all()
    return render(request, 'funcionarios.html', {
        'funcionarios': funcionarios
    })

def movimentacoes(request):
    movimentacoes = Movimentacao.objects.all()
    return render(request, 'movimentacao.html', {
        'movimentacoes': movimentacoes
    })