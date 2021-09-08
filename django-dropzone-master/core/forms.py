from django import forms
from core.models import Pessoa, Image 
from splitjson.widgets import SplitJSONWidget

# Forms do Revisão Manual
class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

# Forms do Revisão Manual
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        # fields = '__all__'
        fields = [
            'language', 
            'image'
        ]
 
class testForm(forms.ModelForm):
    attrs = {'class': 'special', 'size': '40'}
    data = forms.CharField(widget=SplitJSONWidget(attrs=attrs, debug=True))