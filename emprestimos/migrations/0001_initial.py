# Generated by Django 4.1.5 on 2023-02-03 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('editora', models.CharField(max_length=50, verbose_name='Editora')),
                ('quantidade', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('data_do_cadastro', models.DateField(auto_now_add=True)),
                ('autor', models.CharField(max_length=50, verbose_name='Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Codigo')),
                ('data_de_emprestimo', models.DateField(auto_now_add=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='emprestimos.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
