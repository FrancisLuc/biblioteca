from django.forms import ModelForm
from .models import Livro, Emprestimos

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = "__all__"

class EmprestimoForm(ModelForm):
    class meta:
        model = Emprestimos
        fields = "__all__"