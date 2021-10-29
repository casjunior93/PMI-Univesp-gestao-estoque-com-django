from django.contrib import admin

# Register your models here.
from .models import Materiais
from .models import Lotes
from .models import Situacao_material
from .models import Historico_material
from .models import Pessoas
from .models import Movimentacao

@admin.register(Materiais)
class MateriaisAdmin(admin.ModelAdmin):
    #pass
    list_display = ['nome', 'id_material', 'unidade', 'tipo', 'criado']

@admin.register(Lotes)
class LotesAdmin(admin.ModelAdmin):
    #pass
    list_display = ['id_lote', 'controle', 'validade_ca', 'tipo', 'criado']

@admin.register(Situacao_material)
class LotesAdmin(admin.ModelAdmin):
    #pass
    list_display = ['id_lote', 'id_material', 'quantidade', 'localizacao', 'criado', 'atualizado']

@admin.register(Historico_material)
class Historico_materialAdmin(admin.ModelAdmin):
    #pass
    list_display = ['id_lote', 'id_material', 'quantidade', 'localizacao', 'criado', 'atualizado']

@admin.register(Pessoas)
class PessoasAdmin(admin.ModelAdmin):
    #pass
    list_display = ['id_pessoa', 'nome_completo', 'funcao', 'criado', 'atualizado']

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    #pass
    list_display = ['id_movimentacao', 'id_pessoa', 'id_lote', 'id_material', 'quantidade', 'localizacao', 'criado', 'atualizado']