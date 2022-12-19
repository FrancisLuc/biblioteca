from django.db import models

# Create your models here.

class Livros(models.Model):
    titulo = models.CharField('Titulo', max_length=200)
    descricao = models.CharField('Descrição', max_length=500)
    editora = models.CharField('Editora', max_length=200)
    quantidade = models.PositiveIntegerField('Quantidade')
    data_do_cadastro = models.DateField('Data do Cadastro')
    autor = models.CharField('Autor', max_length=200)

    def __str__(self) -> str:
        return self.titulo