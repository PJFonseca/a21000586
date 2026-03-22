from django.db import models

# Create your models here.

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    local = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
class genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    festival = models.ManyToManyField(Festival, on_delete=models.CASCADE)
    genero = models.ForeignKey(genero, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome