from django.forms import ModelForm
from .models import Livros

class LivroForm(ModelForm):
    class meta:
        model = Livros
        fields = ['titulo', 'descricao','editora', 'quantidade', 'data_do_cadastro', 'autor']