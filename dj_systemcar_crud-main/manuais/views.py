from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView, FormView
from django.views.generic.base import TemplateView 
from manuais.forms import carrosForm, RevisaomanualForm, ArquivosForm
from manuais.models import carros, RevisaoManuais, Arquivos

# --- carros views --- #
class carrosIndexView(TemplateView):
	template_name = 'carro/index-carros.html'

class carrosNewView(CreateView):
	template_name = 'carro/carro-novo.html'
	form_class = carrosForm
	success_url = reverse_lazy('carros')
	success_message = 'carro Cadastrado com sucesso'

class carrosDeleteView(DeleteView):
	model = carros
	template_name = 'carro/carro-delete.html'
	success_url = reverse_lazy('carros')
	success_message = 'O carro foi deletado com sucesso'

class carrosUpdateView(UpdateView):
	model = carros
	form_class = carrosForm
	template_name = 'carro/carro-alterar.html'
	success_url = reverse_lazy('carros')
	success_message = 'As alterações foram efectuadas com sucesso'

class carrosListView(ListView):
	model = carros
	template_name = 'carro/carros.html'

# --- manuais views --- #
class ManuaisIndexView(TemplateView):
	template_name = 'manuais/index-manuais.html'

class ManuaisNewView(CreateView):
	template_name = 'manuais/manual-novo.html'
	form_class = RevisaomanualForm
	model = RevisaoManuais 

	def get_success_url(self) -> str:
		messages.success(self.request, 'Manual Cadastrado com sucesso')
		return reverse_lazy('carros')

class ManuaisDeleteView(DeleteView):
	model = RevisaoManuais  
	template_name = 'manuais/manual-delete.html' 

	def get_success_url(self):
		messages.success(self.request, 'O manual foi deletado com sucesso')
		return reverse_lazy('manuais', kwargs = {'pk': self.object.nome_carro.id })

class ManuaisUpdateView(UpdateView):
    model = RevisaoManuais
    form_class = RevisaomanualForm
    template_name = 'manuais/manual-alterar.html'
    def get_success_url(self) -> str:
        messages.success(self.request, 'Manual Cadastrado com sucesso')
        return reverse_lazy('carros')

class ManuaisListView(ListView):
	model = RevisaoManuais
	template_name = 'manuais/manuais.html'
	context_object_name = 'manuais_list' 
	def get_queryset(self):  
		return RevisaoManuais.objects.filter(nome_carro_id=self.kwargs['pk'])



# --- arquivos views --- #

class JSONListView(ListView):
    model = Arquivos 
    template_name = "arquivos/arquivos_list.html"
	


class JSONDetailView(DetailView):
    model = Arquivos 
    template_name = "arquivos/arquivos_detail.html"


class JSONUpdate(UpdateView):
    model = Arquivos
    form_class = ArquivosForm
#    fields = ['name', 'data']
    template_name = "arquivos/arquivo_update.html"


class JSONDelete(DeleteView):
    model = Arquivos
    template_name = "arquivos/arquivo_delete.html"
    success_url = reverse_lazy('arquivos-list')
 

class ArquivosCreate(CreateView):
    model = Arquivos
    form_class = ArquivosForm
    template_name = "arquivos/testcreate.html"
    success_url = '/thanks/'