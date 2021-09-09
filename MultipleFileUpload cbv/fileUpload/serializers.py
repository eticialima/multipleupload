from django.urls import path, include 
from rest_framework import routers, serializers, viewsets
from .models import PersonPhoto, Person

# Serializers define the API representation. 
class PersonPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonPhoto
        fields = ['id', 'photo', 'person']

class PersonSerializer(serializers.ModelSerializer): 
    photos = PersonPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'photos']