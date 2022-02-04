from django.db import models
from django.db.models import JSONField 
from django.urls import reverse
# Create your models here   
from django.urls import reverse
from cloudinary.models import CloudinaryField

class carros(models.Model):
    nome_carro = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    idfonte = models.CharField(max_length=11)

    def __str__(self):
        return "{} ({})".format(self.nome_carro, self.modelo)

class RevisaoManuais(models.Model):
    nome_carro = models.ForeignKey(carros, on_delete=models.PROTECT, related_name="manuais")
    ns_min = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='manuais/pdf')

    def __str__(self):
        return self.nome_carro.nome_carro

 
class Arquivos(models.Model):
    name = models.CharField(max_length=200)
    data  = JSONField()

    def get_absolute_url(self):
        return reverse('arquivos-detail', kwargs={'pk': self.pk})
 
    def __str__(self):
        return self.name
 


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, help_text='identificador baseado no titulo', unique=True)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    created = models.DateField('Criado em', auto_now_add=True)
    modified = models.DateField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('Imagem', blank=True, null=True)
    description = models.CharField('Descrição', max_length=200, blank=True, default='')

    def __str__ (self):
        return self.product.name
    
    class Meta:
        verbose_name = 'Imagem Produto'
        verbose_name = 'Imagens do produto'