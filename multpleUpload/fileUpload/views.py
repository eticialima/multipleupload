from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.utils import timezone 
from django.urls import reverse_lazy 
from rest_framework import viewsets
from .forms import PersonForm
from .models import PersonPhoto, Person
from .serializers import PersonPhotoSerializer, PersonSerializer

# serializar


class PersonSerializerViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonPhotoSerializerViewSet(viewsets.ModelViewSet):
    queryset = PersonPhoto.objects.all()
    serializer_class = PersonPhotoSerializer

# Django template view normal usando classBasedViews


class PersonNewView(CreateView):
    template_name = 'create.html'
    form_class = PersonForm
    success_url = reverse_lazy('home')
    success_message = 'Person Cadastrado com sucesso'

    def post(self, request, **kwargs):
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            person = form.save()
            files = request.FILES.getlist('photos')
            if files:
                for f in files:
                    PersonPhoto.objects.create(person=person, photo=f)
        context = {
            'title': 'Multiple File Upload | Home',
            'form': form
        }
        return self.form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, 'Cadastrado com sucesso')
        return reverse_lazy('home')
 

class PostPersonPhoto(ListView):
    template_name = 'list.html'
    form_class = PersonPhoto
    model = Person


class PostDetailPhoto(DetailView):
    template_name = 'details.html' 
    model = PersonPhoto
    
    def get_object(self):
        id= self.kwargs.get('id')
        return get_object_or_404(Person, id=id)
    
    
     
# FMView
# def home(request):
# 	form = PersonForm
# 	if request.method == 'POST':
# 		form = PersonForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			person = form.save()
# 			files = request.FILES.getlist('photos')
# 			if files:
# 				for f in files:
# 					PersonPhoto.objects.create(person=person, photo=f)
# 	context = {
# 		'title': 'Multiple File Upload | Home',
# 		'form': form
# 	}
# 	return render(request, 'home.html', context)
 
