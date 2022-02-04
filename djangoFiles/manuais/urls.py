from django.urls import path, re_path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from manuais.views import (carrosDeleteView, carrosListView, carrosNewView, carrosUpdateView, ManuaisDeleteView, ManuaisListView, ManuaisNewView, ManuaisUpdateView)
from manuais.views import ArquivosCreate, JSONListView, JSONDetailView, JSONUpdate, JSONDelete

# app_name = "equipment"

urlpatterns = [ 
	path('', carrosListView.as_view(), name='carros'), 
	path('carro-novo/', carrosNewView.as_view(), name='carro-novo'),
	path('<int:pk>/alterar/', carrosUpdateView.as_view(), name='carro-alterar'),
	path('<int:pk>/delete/', carrosDeleteView.as_view(), name='carro-delete'), 
 
	path('carros/<int:pk>/', ManuaisListView.as_view(), name='manuais'), 
	path('manual-novo/', ManuaisNewView.as_view(), name='manual-novo'), 
	path('alterar/<int:pk>/', ManuaisUpdateView.as_view(), name='manual-alterar'),
	path('delete/<int:pk>', ManuaisDeleteView.as_view(), name='manual-delete'),  


	path('arquivos-list/', JSONListView.as_view(), name='arquivos-list'),
        path('arquivos-Detail/<int:pk>/', JSONDetailView.as_view(), name='arquivos-detail'),
        path('arquivos-Update/<int:pk>/', JSONUpdate.as_view(), name='arquivos-update'),
        path('arquivos-Delete/<int:pk>/', JSONDelete.as_view(), name='arquivos-delete'),
        path('new-arquivos/', ArquivosCreate.as_view(), name='arquivos-new'),

] 
