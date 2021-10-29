from django.shortcuts import render

# Create your views here.
from django.http import Http404
from .models import Materiais


def home(request):
    return render(request,'home.html')
