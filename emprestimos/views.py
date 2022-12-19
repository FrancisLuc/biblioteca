from django.shortcuts import render, redirect
from .models import Livros
from .forms import LivroForm
# Create your views here.

def home(request):
    livros = Livros.objects.all()
    return render(request, 'home.html')

def cadastrar_livro(request):
    form = LivroForm
    return render(request, 'fazer_emprestimo.html', {"form": form})
