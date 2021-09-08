from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Image, Pessoa
from rest_framework import routers, serializers, viewsets
from .serializers import PessoaSerializer, ImageSerializer
from core.forms import ImageForm, PessoaForm, testForm
# Create your views here. 
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView 

from django.shortcuts import render 
from django.template import RequestContext 

# ViewSets define the view behavior.
class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
 
class IndexView(TemplateView):
    template_name='index.html'

# Adiciona Pessoa
class PessoaNewView(CreateView):
    template_name = 'index.html'
    form_class = PessoaForm
    model = Pessoa
    success_url = reverse_lazy('index')
    success_message = 'Pessoa cadastrado com sucesso'
 
 
# def file_upload(request):
#     # print(request.FILES)
#     if request.method == 'POST':
#         my_file=request.FILES.get('file')
#         Image.objects.create(image=my_file)
#         return HttpResponse('')
#     return JsonResponse({'post':'fasle'})

# -*- coding: utf-8 -*-


def test_dict(request):
    json = {'a': 1,
            'b': 2,
            'c': 3,
            'd': 4}
    form = testForm(request.POST or None, initial={'data': json})
    if form.is_valid():
        # validate and save
        pass

    template = 'test_template.html'
    context = RequestContext(request, {'form': form})
    return render(template, context)