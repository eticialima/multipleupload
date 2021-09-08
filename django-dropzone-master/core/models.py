from django.db import models

# Create your models here.

CHOICE_LANGS = [('BR','PORTUGUÊS'),('EN','INGLÊS'),('ES','ESPANHOL'),]

class Pessoa(models.Model):
    nome = models.CharField(max_length=200) 
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome

 
class Image(models.Model): 
    nome = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name="images")
    language = models.CharField(max_length=2, choices=CHOICE_LANGS)  
    image=models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
 
    def __str__(self):
        return str(self.pk)
