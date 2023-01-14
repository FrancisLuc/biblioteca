from django.contrib import admin
from .models import Livro, Emprestimos
 
# Register your models here.

@admin.register(Livro)
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao','editora', 'quantidade', 'data_do_cadastro', 'autor')

@admin.register(Emprestimos)
class EmprestimosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'usuario', 'data_de_emprestimo', 'livro')
