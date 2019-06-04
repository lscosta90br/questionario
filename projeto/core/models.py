from django.db import models
from django.contrib.auth.models import User

ENTRADA_TIPO = (
    ('cb', 'checkbox'),
    ('cl', 'cheklist'),
    ('tx', 'text'),
)

class Pergunta(models.Model):
    descricao = models.CharField(("Descrição"), max_length=200)
    entrada_tipo = models.CharField(("Entrada tipo"), choices=ENTRADA_TIPO ,max_length=2)
    criando_em = models.DateField(("Criando em"), auto_now_add=True, blank=True, null=True)
    atualizado_em = models.DateTimeField(("Atualizado em"), auto_now_add=True, blank=True, null=True)
    enquete = models.ManyToManyField("enquete", verbose_name=("Enquete"))
    perguntaresposta = models.ForeignKey('PerguntaResposta', on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = ''
        managed = True
        verbose_name =  'Pergunta'
        verbose_name_plural =  'Perguntas'


STATUS = (
    ('c', 'certo'),
    ('e', 'errado'),
)
class Resposta(models.Model):
    descricao = models.CharField(("Descrição"), max_length=200)
    status = models.CharField(("status"), choices=STATUS ,max_length=1)
    pergunta = models.ForeignKey('pergunta', on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'

class Enquete(models.Model):
    titulo = models.CharField(("Título"), max_length=50, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Enquete'
        verbose_name_plural = 'Enquetes'

TIPO_PERGUNTA_RESPOSTA = (
    ('enquete', 'enquete'),
    ('questionario', 'questionario'),
    ('prova', 'prova'),
)
class PerguntaResposta(models.Model):
    titulo = models.CharField(("Título"), max_length=50, blank=True)
    tipo_pergunta_resposta = models.CharField(("Tipo"), choices=TIPO_PERGUNTA_RESPOSTA, max_length=15)


    def __str__(self):
        return self.titulo

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'PerguntaResposta'
        verbose_name_plural = 'PerguntaRespostas'


class Prova(models.Model):
    descricao = models.CharField(("Descrição"), max_length=50)
    enquete = models.ForeignKey('enquete', on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(User, verbose_name=("Usuarios"))
    #  = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Prova'
        verbose_name_plural = 'Provas'

