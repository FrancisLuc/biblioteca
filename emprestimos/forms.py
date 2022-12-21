from django.forms import ModelForm
from .models import Livro, Emprestimos
from django import forms

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = "__all__"

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimos
        fields = "__all__"