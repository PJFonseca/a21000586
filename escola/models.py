from django.db import models


class Escola (models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nome} - {self.morada}'

class Turma (models.Model):

    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name='escola_turmas')

    def __str__(self):
        return f'{self.ano} - {self.nome}'
    
class Professor (models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    turma = models.OneToOneField(Turma, on_delete=models.CASCADE, related_name='turma_professor')

    def __str__(self):
        return f'{self.nome} - {self.idade} anos'
    
class Aluno (models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    numero = models.IntegerField()
    turma = models.OneToOneField(Turma, on_delete=models.CASCADE, related_name='turma_alunos')

    def __str__(self):
        return f'{self.nome} - {self.idade} anos'