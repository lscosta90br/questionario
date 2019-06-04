# Generated by Django 2.2.1 on 2019-06-02 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=50, verbose_name='Título')),
            ],
            options={
                'verbose_name': 'Enquete',
                'verbose_name_plural': 'Enquetes',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('entrada_tipo', models.CharField(choices=[('cb', 'checkbox'), ('cl', 'cheklist'), ('tx', 'text')], max_length=2, verbose_name='Entrada tipo')),
                ('criando_em', models.DateField(auto_now_add=True, null=True, verbose_name='Criando em')),
                ('atualizado_em', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Atualizado em')),
                ('enquete', models.ManyToManyField(to='core.Enquete', verbose_name='Enquete')),
            ],
            options={
                'verbose_name': 'Pergunta',
                'verbose_name_plural': 'Perguntas',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('status', models.CharField(choices=[('c', 'certo'), ('e', 'errado')], max_length=1, verbose_name='status')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pergunta')),
            ],
            options={
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('enquete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Enquete')),
                ('usuarios', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Usuarios')),
            ],
            options={
                'verbose_name': 'Prova',
                'verbose_name_plural': 'Provas',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
