from django.contrib import admin
from .models import Loja, Categoria, Produto, Cliente, Pedido, ItemPedido

class LojaAdmin(admin.ModelAdmin):
    list_display = ("nome", "morada")
    search_fields = ("nome",)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "loja")
    list_filter = ("loja",)
    search_fields = ("nome",)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "categoria")
    list_filter = ("categoria",)
    search_fields = ("nome",)



class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade", "loja")
    list_filter = ("loja",)
    search_fields = ("nome", "morada")



class PedidoAdmin (admin.ModelAdmin):
    list_display = ("numero", "data", "cliente")
    list_filter = ("cliente",)
    search_fields = ("numero", "data", "cliente")   

class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "produto", "quantidade")
    list_filter = ("pedido",)

admin.site.register(Loja, LojaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)
