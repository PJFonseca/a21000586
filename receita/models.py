from django.db import models

# Create your models here.
class receita (models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)
    receita = models.ForeignKey(receita, on_delete=models.CASCADE, related_name='receita_ingredientes')

    def __str__(self):
        return f'{self.nome} - {self.quantidade}'
    
class utilizador(models.Model):
    nome = models.CharField(max_length=100)
    favorita = models.ForeignKey(receita, on_delete=models.CASCADE, related_name='receita_favoritos')

    def __str__(self):
        return f'A receita favorita do/da {self.nome} é {self.favorita.nome}'
