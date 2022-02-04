# Generated by Django 3.2.11 on 2022-02-04 14:10

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='carros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_carro', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('idfonte', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(help_text='identificador baseado no titulo', max_length=100, unique=True, verbose_name='Identificador')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RevisaoManuais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ns_min', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='manuais/pdf')),
                ('nome_carro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='manuais', to='manuais.carros')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Imagem')),
                ('description', models.CharField(blank=True, default='', max_length=200, verbose_name='Descrição')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='manuais.product')),
            ],
            options={
                'verbose_name': 'Imagens do produto',
            },
        ),
    ]
