#ISTO FOI GERADO COM O CHATGPT, queria apenas um comando para criar dados aleatorios.

from django.core.management.base import BaseCommand
from faker import Faker
import random

from loja.models import Loja, Categoria, Produto, Cliente, Pedido, ItemPedido

fake = Faker()


class Command(BaseCommand):
    help = "Seed database with random data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Cleaning old data...")
        ItemPedido.objects.all().delete()
        Pedido.objects.all().delete()
        Cliente.objects.all().delete()
        Produto.objects.all().delete()
        Categoria.objects.all().delete()
        Loja.objects.all().delete()

        # 🏬 Lojas
        lojas = []
        for _ in range(2):
            loja = Loja.objects.create(
                nome=fake.company(),
                morada=fake.address()
            )
            lojas.append(loja)

        # 📂 Categorias
        categorias = []
        for loja in lojas:
            for _ in range(3):
                cat = Categoria.objects.create(
                    nome=fake.word(),
                    loja=loja
                )
                categorias.append(cat)

        # 📦 Produtos
        produtos = []
        for cat in categorias:
            for _ in range(5):
                prod = Produto.objects.create(
                    nome=fake.word(),
                    preco=round(random.uniform(5, 100), 2),
                    categoria=cat
                )
                produtos.append(prod)

        # 👤 Clientes
        clientes = []
        for loja in lojas:
            for _ in range(5):
                cliente = Cliente.objects.create(
                    nome=fake.name(),
                    morada=fake.address(),
                    idade=random.randint(18, 70),
                    loja=loja
                )
                clientes.append(cliente)

        # 🧾 Pedidos + Itens
        for cliente in clientes:
            for _ in range(random.randint(1, 3)):
                pedido = Pedido.objects.create(
                    numero=random.randint(1000, 9999),
                    data=fake.date_this_year(),
                    cliente=cliente
                )

                # itens do pedido
                for _ in range(random.randint(1, 4)):
                    ItemPedido.objects.create(
                        pedido=pedido,
                        produto=random.choice(produtos),
                        quantidade=random.randint(1, 5)
                    )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))