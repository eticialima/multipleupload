from django import forms

from .models import Person, PersonPhoto

class PersonForm(forms.ModelForm):
    photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Person
        fields = [
            'name',
            'age',
        ]

class PersonPhotoForm(forms.ModelForm):
    class Meta:
        model = PersonPhoto
        fields = ['photo', 'person']