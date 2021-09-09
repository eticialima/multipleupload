from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField('Nome do Personagem',max_length=100)
	age = models.PositiveIntegerField('Idade')

	def __unicode__(self):
		return self.name

class PersonPhoto(models.Model):
	photo = models.FileField('Arquivos',upload_to='image')
	person = models.ForeignKey(Person, related_name='photos', on_delete=models.CASCADE)
	def __unicode__(self):
		return self.photo.url
