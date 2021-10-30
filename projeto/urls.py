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
from gestao_estoque import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('materiais/', views.materiais,name='materiais'),
    path('funcionarios/', views.funcionarios,name='funcionarios'),
    path('movimentacoes/', views.movimentacoes,name='movimentacoes'),
    path('historico/', views.historico,name='historico'),
    path('lotes/', views.lotes,name='lotes'),
    path('situacao_material/', views.situacao,name='situacao')
]
