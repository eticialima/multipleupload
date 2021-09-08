from django.contrib import admin
from .models import carros, RevisaoManuais, Arquivos 
# Register your models here.
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget


admin.site.register(carros)
admin.site.register(RevisaoManuais)

@admin.register(Arquivos)
class ArquivosAdmin(admin.ModelAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
}
 


from manuais.models import Product,  ProductImage
 

admin.site.register(Product, ProductImage)