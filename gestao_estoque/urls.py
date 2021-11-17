"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from gestao_estoque import views
from gestao_estoque.views import FuncionarioCreateView, MaterialCreateView, LoteCreateView, MovimentacaoCreateView, FuncionarioUpdateView, MaterialUpdateView, MaterialDeleteView, FuncionarioDeleteView

app_name = 'gestao_estoque'

urlpatterns = [
    path('',  views.materiais, name='materiais'),
    path('materiais/', views.materiais, name='materiais'),
    path('funcionarios/', views.funcionarios, name='funcionarios'),
    path('movimentacoes/', views.movimentacoes, name='movimentacoes'),
    path('historico/', views.historico, name='historico'),
    path('lotes/', views.lotes, name='lotes'),
    path('situacao_material/', views.situacao, name='situacao'),
    path('funcionarios/cadastrar/', FuncionarioCreateView.as_view()),
    path('materiais/cadastrar/', MaterialCreateView.as_view()),
    path('lotes/cadastrar/', LoteCreateView.as_view()),
    path('movimentacoes/cadastrar/', MovimentacaoCreateView.as_view()),
    path('funcionarios/editar/<int:pk>', FuncionarioUpdateView.as_view()),
    path('materiais/editar/<int:pk>', MaterialUpdateView.as_view(), name='atualiza_material'),
    path('materiais/excluir/<int:pk>', MaterialDeleteView.as_view()),
    path('funcionarios/excluir/<int:pk>', FuncionarioDeleteView.as_view())
]
