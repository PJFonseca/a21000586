from django.contrib import admin
from .models import receita, ingrediente, utilizador
# Register your models here.

class receitaAdmin (admin.ModelAdmin):
    list_display=("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)       

class ingredienteAdmin (admin.ModelAdmin):
    list_display=("nome", "quantidade", "receita")
    ordering = ("nome", "quantidade", "receita")
    search_fields = ("nome", "quantidade", "receita")

class utilizadorAdmin (admin.ModelAdmin):
    list_display=("nome", "favorita")
    ordering = ("nome", "favorita")
    search_fields = ("nome", "favorita")  

admin.site.register(receita, receitaAdmin)
admin.site.register(ingrediente, ingredienteAdmin)
admin.site.register(utilizador, utilizadorAdmin)
