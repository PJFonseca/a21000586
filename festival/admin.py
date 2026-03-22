from django.contrib import admin

# Register your models here.

from .models import Festival, genero, banda

class FestivalAdmin (admin.ModelAdmin):
    list_display=("nome", "data_inicio", "data_fim", "local")
    ordering = ("nome", "data_inicio", "data_fim", "local")
    search_fields = ("nome", "data_inicio", "data_fim", "local")    

class generoAdmin (admin.ModelAdmin):
    list_display=("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)   

class bandaAdmin (admin.ModelAdmin):
    list_display=("nome", "genero", "festival")
    ordering = ("nome", "genero", "festival")
    search_fields = ("nome", "genero", "festival")  

admin.site.register(Festival)
admin.site.register(genero)
admin.site.register(banda)  
