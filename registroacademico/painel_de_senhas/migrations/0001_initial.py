# Generated by Django 2.2 on 2021-11-17 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='StatusSenha',
            fields=[
                ('id_status_senha', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_tipo', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Senha',
            fields=[
                ('id_senha', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('senha', models.IntegerField(max_length=40)),
                ('hora_data', models.DateTimeField(auto_now_add=True)),
                ('Categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painel_de_senhas.Categoria')),
                ('StatusSenha_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painel_de_senhas.StatusSenha')),
                ('Tipo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painel_de_senhas.Tipo')),
            ],
        ),
    ]
