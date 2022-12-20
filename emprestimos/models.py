from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    descricao = models.CharField('Descrição', max_length=500)
    editora = models.CharField('Editora', max_length=50)
    quantidade = models.IntegerField('Quantidade')
    data_do_cadastro = models.DateField('Data do Cadastro')
    autor = models.CharField('Autor', max_length=50)

    def __str__(self):
        return self.titulo

class Emprestimos(models.Model):
    codigo = models.BigIntegerField('Codigo')
    usuario = models.CharField('Usuario', max_length=50)
    data_de_emprestimo = models.DateField('Data de Emprestimo')
    livro = models.CharField('Livro', max_length=50)

    def __str__(self):
        return self.codigo