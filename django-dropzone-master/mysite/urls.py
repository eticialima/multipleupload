"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import PessoaViewSet, ImageViewSet  
from rest_framework import routers, serializers, viewsets



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'images', ImageViewSet)



urlpatterns = [
     # serializers 
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # normal
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
