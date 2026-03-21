from django.db import models


class ginasio(models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nome} - {self.morada}'

class membro(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    numero = models.IntegerField()
    ginasio = models.ForeignKey(ginasio, on_delete=models.CASCADE, related_name='ginasio_membros')

    def __str__(self):
        return f'{self.nome} - {self.idade} anos - {self.numero}'
    
class instrutor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    ginasio = models.ForeignKey(ginasio, on_delete=models.CASCADE, related_name='ginasio_instrutores')

    def __str__(self):
        return f'{self.nome} - {self.idade} anos'   

class sessao(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()      
    instrutor = models.ForeignKey(instrutor, on_delete=models.CASCADE, related_name='instrutor_sessoes')
    membro = models.ForeignKey(membro, related_name='membro_sessoes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.data} - {self.hora} - {self.instrutor.nome} - {self.membro.nome}'
    
class Meta:
    unique_together = ('instrutor', 'data', 'hora')