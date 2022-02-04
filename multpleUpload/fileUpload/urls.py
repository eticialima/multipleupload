
from django.urls import path 
from fileUpload.views import PersonNewView 
 
urlpatterns = [ 
    path('', PersonNewView.as_view(), name='home'), 
]