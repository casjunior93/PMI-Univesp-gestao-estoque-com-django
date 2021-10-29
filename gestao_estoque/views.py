from django.shortcuts import render

# Create your views here.
from django.http import Http404
from .models import Materiais
from .models import Pessoas


def home(request):
    return render(request,'home.html')

def materiais(request):
    materiais = Materiais.objects.all()
    return render(request, 'materiais.html', {
        'materiais': materiais
    })

def materiais(request):
    funcionarios = Pessoas.objects.all()
    return render(request, 'funcionarios.html', {
        'funcionarios': funcionarios
    })
