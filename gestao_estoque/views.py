from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
from django.http import Http404
from .models import Historico_material, Materiais
from .models import Pessoas
from .models import Movimentacao
from .models import Historico_material
from .models import Lotes
from .models import Situacao_material


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

def lotes(request):
    lotes = Lotes.objects.all()
    return render(request, 'lotes.html', {
        'lotes': lotes
    })

def situacao(request):
    situacao = Situacao_material.objects.all()
    return render(request, 'situacao_material.html', {
        'situacao': situacao
    })

class FuncionarioCreateView(CreateView):
  template_name = 'cadastro_funcionario.html'
  model = Pessoas
  fields = ['nome_completo', 'funcao']
  success_url = reverse_lazy("funcionarios")
