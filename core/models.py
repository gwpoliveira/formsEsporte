from django.db import models

class FormularioEsporte(models.Model):
    UNIDADES = [
        ('Primavera', 'Magister Primavera'),

    ]

    ATIVIDADES = [
        ('Xadrez', 'Xadrez'),
        ('Dama', 'Dama'),
        ('Queimada', 'Queimada'),
        ('Ping pong', 'Ping pong'),
        ('Basquete arremesso', 'Basquete arremesso'),
        ('Basquete dupla', 'Basquete dupla'),
        ('Futebol de Salão', 'Futebol de Salão'),
        ('Vôlei', 'Vôlei'),
        ('Handebol', 'Handebol'),
        ('Futebol de botão', 'Futebol de botão'),
    ]

    nome = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
    idade = models.IntegerField()
    unidade = models.CharField(max_length=20, choices=UNIDADES)
    responsavel = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    atividades = models.ManyToManyField('core.Atividade')

class Atividade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
