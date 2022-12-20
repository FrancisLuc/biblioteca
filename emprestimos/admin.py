from django.contrib import admin
from .models import Livro
 
# Register your models here.

@admin.register(Livro)
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao','editora', 'quantidade', 'data_do_cadastro', 'autor')