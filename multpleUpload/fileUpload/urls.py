
from django.urls import path 
from fileUpload import views
 
urlpatterns = [ 
    path('', views.PersonNewView.as_view(), name='create'), 
    path('list/', views.PostPersonPhoto.as_view(), name='list'),
    path('post-detail/<int:id>/', views.PostDetailPhoto.as_view(), name='post-detail'), 
]