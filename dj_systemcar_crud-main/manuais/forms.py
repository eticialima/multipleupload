from django import forms
from manuais.models import carros, RevisaoManuais, Arquivos
from django_json_widget.widgets import JSONEditorWidget


# Forms do Carro
class carrosForm(forms.ModelForm):
    class Meta:
        model = carros
        fields = '__all__'

# Forms do Revisão Manual
class RevisaomanualForm(forms.ModelForm):
    class Meta:
        model = RevisaoManuais
        fields = '__all__'
 

 

# Forms do Arquivos
class ArquivosForm(forms.ModelForm): 
    class Meta:
        model = Arquivos
        fields = ('name', 'data')
        widgets = {'data': JSONEditorWidget}



