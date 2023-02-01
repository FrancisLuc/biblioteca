from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Emprestimos
from .forms import LivroForm, EmprestimoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.db import models
# Create your views here.

def home(request):
    livros = Livro.objects.all()
    context = {"livros": livros}
    return render(request, 'home.html', context)

@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save()
            return redirect('/')
    else:
        form = LivroForm()
        context = {
            'form': form
        }
        return render(request, 'cadastrar_livro.html', context=context)

@login_required
def fazer_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save()
            return redirect('/')
    else:
        form = EmprestimoForm()
        context = {
            'form': form
        }
        return render(request, 'fazer_emprestimo.html', context=context)

def listar_livros(request):
    livros = Livro.objects.all()
    context = {"livros": livros}
    return render(request, 'listar_livros.html', context)

@login_required
def historico_de_emprestimos(request):
    emprestimos = Emprestimos.objects.all()
    context = {"emprestimos": emprestimos}
    return render(request, 'historico_de_emprestimos.html', context=context)
    
def detalhar_livro(request, id):
    livro = Livro.objects.get(id=id)
    return render(request, 'detalhar_livro.html', {'livro': livro})

@login_required
def deletar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    livro.delete()
    return redirect('/')

@login_required
def atualizar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    form = LivroForm(instance=livro)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro = form.save()
            return redirect('/')
        else:
            return render(request, 'atualizar_livro.html', {'form': form, 'livro': livro})
    else:
        return render(request, 'atualizar_livro.html', {'form': form, 'livro': livro})

@login_required
def emprestar_livro(request, id):
    emprestimo_livro = get_object_or_404(Livro, pk=id)
    emprestimo = Emprestimos()
    emprestimo.livro = emprestimo_livro
    emprestimo.usuario = request.user
    emprestimo.save()
    livro = Livro.objects.filter(pk=id)
    livro.update(quantidade=models.F('quantidade') - 1)
    return redirect('/')

@login_required
def devolver_livro(request, id):
    emprestimo = get_object_or_404(Emprestimos, pk=id)
    livro = Livro.objects.filter(pk=emprestimo.livro.id)
    livro.update(quantidade =models.F('quantidade') + 1)
    emprestimo.delete()
    return redirect('/historico_de_emprestimos/')

class SingUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'