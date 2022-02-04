from django.views.generic.edit import CreateView
from django.contrib import messages
from django.shortcuts import render
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
    template_name = 'home.html'
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
 
