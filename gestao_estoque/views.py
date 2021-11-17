from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.forms.widgets import SelectDateWidget
from .forms import MaterialForm, MovimentacaoForm, FuncionarioForm, MaterialUpdateForm
from django.db.models import F

# Create your views here.
from django.http import Http404
from .models import Historico_material, Materiais
from .models import Pessoas
from .models import Movimentacao
from .models import Historico_material
from .models import Lotes
from .models import Situacao_material


def home(request):
    return render(request, 'home.html')


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
    return render(request, 'situacao-material.html', {
        'situacao': situacao
    })


class FuncionarioCreateView(CreateView):
    template_name = 'cadastro-funcionario.html'
    model = Pessoas
    form_class = FuncionarioForm
    success_url = reverse_lazy("funcionarios")


class MaterialCreateView(CreateView):
    template_name = 'cadastro-material.html'
    model = Materiais
    form_class = MaterialForm
    success_url = reverse_lazy("materiais")

class LoteCreateView(CreateView):
    template_name = 'cadastro-lote.html'
    model = Lotes
    fields = ['id_material', 'controle', 'validade_ca', 'tipo', 'quantidade']
    success_url = reverse_lazy("lotes")
    template_name_suffix = '_cadastro_lote'
    def get_form(self):
        '''add date picker in forms'''
        form = super(LoteCreateView, self).get_form()
        form.fields['validade_ca'].widget = SelectDateWidget()
        return form


class MovimentacaoCreateView(CreateView):
    template_name = 'cadastro-movimentacao.html'
    model = Movimentacao
    form_class = MovimentacaoForm

    def form_valid(self, form):
        if form.is_valid():
            """ Salva movimentação e desconta na quantidade do lote """
            lote_controle = form.cleaned_data['id_lote']
            obj = Lotes.objects.get(controle=lote_controle)
            Lotes.objects.filter(pk=obj.id_lote).update(quantidade=F('quantidade') - form.cleaned_data['quantidade'])
            nova_movimentacao = form.save()
            """ Adiciona Historico """
            h = Historico_material(id_lote=form.cleaned_data['id_lote'], id_material=form.cleaned_data['id_material'], quantidade=form.cleaned_data['quantidade'], localizacao=form.cleaned_data['localizacao'])
            h.save()
            return redirect('movimentacoes')

class MaterialUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Materiais
    form_class = MaterialUpdateForm

    def get_object(self, queryset=None):
      material = None

      # Se você utilizar o debug, verá que os 
      # campos {pk} e {slug} estão presente em self.kwargs
      id = self.kwargs.get(self.pk_url_kwarg)
      slug = self.kwargs.get(self.slug_url_kwarg)

      if id is not None:
        # Busca o funcionario apartir do id
        material = Materiais.objects.filter(id=id).first()

      elif slug is not None:        
        # Pega o campo slug do Model
        campo_slug = self.get_slug_field()

        # Busca o funcionario apartir do slug
        material = Materiais.objects.filter(**{campo_slug: slug}).first()

      # Retorna o objeto encontrado
      return material

class FuncionarioUpdateView(UpdateView):
    template_name = "atualiza.html"
    model = Pessoas
    fields = '__all__'
    context_object_name = 'funcionario'

    def get_object(self, queryset=None):
      funcionario = None

      # Se você utilizar o debug, verá que os 
      # campos {pk} e {slug} estão presente em self.kwargs
      id = self.kwargs.get(self.pk_url_kwarg)
      slug = self.kwargs.get(self.slug_url_kwarg)

      if id is not None:
        # Busca o funcionario apartir do id
        funcionario = Pessoas.objects.filter(id=id).first()

      elif slug is not None:        
        # Pega o campo slug do Model
        campo_slug = self.get_slug_field()

        # Busca o funcionario apartir do slug
        funcionario = Pessoas.objects.filter(**{campo_slug: slug}).first()

      # Retorna o objeto encontrado
      return funcionario