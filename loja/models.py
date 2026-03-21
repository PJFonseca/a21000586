from django.db import models

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='categorias')

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=200)  # ✔ morada única por cliente
    idade = models.IntegerField()
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='clientes')

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    numero = models.IntegerField()
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')

    def __str__(self):
        return f'Pedido {self.numero}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.produto.nome} x {self.quantidade}'