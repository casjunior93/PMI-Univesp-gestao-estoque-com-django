from django.db import models

# Create your models here.


class Materiais(models.Model):
    TIPOS = [('0', 'Material'), ('1', 'EPI')]
    id_material = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    unidade = models.SmallIntegerField(default=0)
    tipo = models.CharField(max_length=1, choices=TIPOS, blank=True)
    criado = models.DateTimeField(auto_now_add=True)

    # alterando a exibição no painel do Admin
    def __str__(self):
        return self.nome


class Lotes(models.Model):
    TIPOS = [('0', 'Material'), ('1', 'EPI')]
    id_lote = models.AutoField(primary_key=True)
    controle = models.CharField(max_length=30, null=True)
    validade_ca = models.DateField(null=True)
    tipo = models.CharField(max_length=1, choices=TIPOS, blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    quantidade = models.FloatField(default=0)
    
    # alterando a exibição no painel do Admin

    def __str__(self):
        return self.controle


class Situacao_material(models.Model):
    id_lote = models.ForeignKey('Lotes', on_delete=models.CASCADE, blank=True)
    id_material = models.ForeignKey(
        'Materiais', on_delete=models.CASCADE, blank=True)
    quantidade = models.FloatField(default=0)
    localizacao = models.CharField(max_length=100, blank=False, default='--')
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)


class Historico_material(models.Model):
    id_lote = models.ForeignKey('Lotes', on_delete=models.CASCADE, blank=True)
    id_material = models.ForeignKey(
        'Materiais', on_delete=models.CASCADE, blank=True)
    quantidade = models.FloatField(default=0)
    localizacao = models.CharField(max_length=100, blank=False, default='--')
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)


class Pessoas(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length=255)
    funcao = models.CharField(max_length=30, null=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    # alterando a exibição no painel do Admin

    def __str__(self):
        return self.nome_completo


class Movimentacao(models.Model):
    id_movimentacao = models.AutoField(primary_key=True)
    id_pessoa = models.ForeignKey(
        'Pessoas', on_delete=models.CASCADE, blank=True)
    id_lote = models.ForeignKey('Lotes', on_delete=models.CASCADE, blank=True)
    id_material = models.ForeignKey(
        'Materiais', on_delete=models.CASCADE, blank=True)
    quantidade = models.FloatField()
    localizacao = models.CharField(max_length=100, blank=False, default='--')
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
