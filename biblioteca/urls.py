"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emprestimos.views import home, cadastrar_livro, fazer_emprestimo, listar_livros, historico_de_emprestimos, detalhar_livro, deletar_livro, atualizar_livro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('cadastrar_livro/', cadastrar_livro, name="cadastrar_livro"),
    path('fazer_emprestimo/', fazer_emprestimo, name="fazer_emprestimo"),
    path('listar_livros/', listar_livros, name="listar_livros"),
    path('historico_de_emprestimos/', historico_de_emprestimos, name="historico_de_emprestimos"),
    path('detalhar_livro/<int:id>/', detalhar_livro, name="detalhar_livro"),
    path('deletar_livro/<int:id>/', deletar_livro, name="deletar_livro")
    path('atualizar_livro/<int:id>/', atualizar_livro, name="atualizar_livro")
]
