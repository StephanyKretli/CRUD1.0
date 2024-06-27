from django.db import models 


# Create your models here.
class Usuarios (models.Model):
    nome = models.CharField(max_length=150)
    data_nasc = models.DateField(auto_now=False, auto_now_add=False)
    cpf = models.CharField(max_length=11)
    data_cad = models.DateField(auto_now=False, auto_now_add=False)
