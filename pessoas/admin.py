from django.contrib import admin

from escola.models import Aluno, Escola, Professor, Turma   
from .models import Pessoa

class PessoaAdmin (admin.ModelAdmin):
    list_display=("nome", "idade")
    ordering = ("nome", "idade")
    search_fields = ("nome", "idade")


class EscolaAdmin (admin.ModelAdmin):
    list_display=("nome", "morada")
    ordering = ("nome", "morada")
    search_fields = ("nome", "morada")

class TurmaAdmin (admin.ModelAdmin):
    list_display=("nome", "ano")
    ordering = ("ano", "nome")
    search_fields = ("nome", "ano")

class ProfessorAdmin (admin.ModelAdmin):
    list_display=("nome", "idade")
    ordering = ("nome", "idade")
    search_fields = ("nome", "idade")

class AlunoAdmin (admin.ModelAdmin):
    list_display=("nome", "idade", "numero")
    ordering = ("nome", "idade", "numero")
    search_fields = ("nome", "idade", "numero")



admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Escola, EscolaAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)