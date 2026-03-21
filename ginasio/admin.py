from django.contrib import admin

from ginasio.models import ginasio, instrutor, membro, sessao

# Register your models here.
class ginasioAdmin (admin.ModelAdmin):
    list_display=("nome", "morada")
    ordering = ("nome", "morada")
    search_fields = ("nome", "morada")

class instrutorAdmin (admin.ModelAdmin):    
    list_display=("nome", "idade")
    ordering = ("nome", "idade")
    search_fields = ("nome", "idade")   

class membroAdmin (admin.ModelAdmin):
    list_display=("nome", "idade", "numero", "ginasio")
    ordering = ("nome", "idade", "numero", "ginasio")
    search_fields = ("nome", "idade", "numero", "ginasio")  

class sessaoAdmin (admin.ModelAdmin):
    list_display=("nome", "data", "hora", "instrutor", "membro")
    ordering = ("nome", "data", "hora", "instrutor", "membro")
    search_fields = ("nome", "data", "hora", "instrutor", "membro")

admin.site.register(ginasio)
admin.site.register(instrutor)
admin.site.register(membro)
admin.site.register(sessao) 