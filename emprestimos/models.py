from django.db import models
import uuid

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    descricao = models.TextField('Descrição')
    editora = models.CharField('Editora', max_length=50)
    quantidade = models.PositiveIntegerField('Quantidade')
    data_do_cadastro = models.DateField(auto_now_add=True)
    autor = models.CharField('Autor', max_length=50)

    def __str__(self):
        return self.titulo

class Emprestimos(models.Model):
    codigo = models.UUIDField('Codigo', default=uuid.uuid4, editable=False)
    usuario = models.CharField('Usuario', max_length=50)
    data_de_emprestimo = models.DateField(auto_now_add=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigo)