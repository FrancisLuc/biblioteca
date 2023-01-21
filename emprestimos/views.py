from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Emprestimos
from .forms import LivroForm, EmprestimoForm
# Create your views here.

def home(request):
    livros = Livro.objects.all()
    context = {"livros": livros}
    return render(request, 'home.html', context)

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

def historico_de_emprestimos(request):
    emprestimos = Emprestimos.objects.all()
    context = {"emprestimos": emprestimos}
    return render(request, 'historico_de_emprestimos.html', context=context)

def detalhar_livro(request, id):
    livro = Livro.objects.get(id=id)
    return render(request, 'detalhar_livro.html', {'livro': livro})

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    livro.delete()
    return redirect('/')

def atualizar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    form = LivroForm(instance=livro)
    if request.method == "POST":