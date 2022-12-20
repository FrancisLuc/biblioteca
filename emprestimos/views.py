from django.shortcuts import render
from .models import Livro
from .forms import LivroForm, EmprestimoForm
# Create your views here.

def home(request):
    livro = Livro.objects.all()
    return render(request, 'home.html', {'livro': livro})

def cadastrar_livro(request):
    form = LivroForm()
    context = {
        'form': form
    }
    return render(request, 'cadastrar_livro.html', context=context)

def fazer_emprestimo(request):
    form = EmprestimoForm()
    context = {
        'form': form
    }
    return render(request, 'fazer_emprestimo.html', context=context)