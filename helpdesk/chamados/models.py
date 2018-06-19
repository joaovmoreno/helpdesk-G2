from django.db import models
from django.contrib.auth.models import User

import datetime



class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=128)

    def __str__(self):
        return self.titulo


class StatusChamado(models.Model):
    titulo = models.CharField(max_length=120)

    def __str__(self):
        return self.titulo


class Funcionario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=10)
    nome = models.CharField(max_length=128)
    
    def __str__(self):
        return '{}-{}'.format(self.matricula, self.nome)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'


class Chamado(models.Model):
    id = models.AutoField(primary_key=True)
    criado_por = models.ForeignKey(Funcionario, related_name='criado_por', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name='categoria', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=128)
    descricao = models.TextField()
    telefone = models.CharField(max_length=11)
    data_abertura = models.DateTimeField(default=datetime.datetime.now())
    status = models.ForeignKey(StatusChamado, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Atendimento(models.Model):
    atendente = models.ForeignKey(Funcionario, related_name='atendente', on_delete=models.CASCADE)
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_atendimento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Atendimento do chamado #{}'.format(self.chamado)




