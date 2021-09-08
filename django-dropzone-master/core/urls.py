from django.urls import path 
from core.views import (PessoaNewView, IndexView)

urlpatterns = [ 
    path('', IndexView.as_view(), name='index'), 
	#path('pessoa/', PessoaNewView.as_view(), name='pessoa'), 
 
    #path('upload/', views.file_upload),
]