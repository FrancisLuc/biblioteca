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