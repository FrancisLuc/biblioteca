from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm, EmprestimoForm
# Create your views here.

def home(request):
    livros = Livro.objects.all()
    return render(request, 'home.html', {'livros': livros})

def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save()
            return redirect('home/')
    else:
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