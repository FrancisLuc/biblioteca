from django.contrib import admin
from .models import Livros
 
# Register your models here.

@admin.register(Livros)
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao','editora', 'quantidade', 'data_do_cadastro', 'autor')