from django.shortcuts import render

# Create your views here.
from django.http import Http404
from .models import Historico_material, Materiais
from .models import Pessoas
from .models import Movimentacao
from .models import Historico_material


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

def historico(request):
    historico = Historico_material.objects.all()
    return render(request, 'historico.html', {
        'historico': historico
    })