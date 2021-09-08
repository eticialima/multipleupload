from django.urls import path, include
from .models import Pessoa, Image
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['nome', 'language', 'image']
 
class PessoaSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'images']