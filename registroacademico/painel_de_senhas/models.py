from django.db import models

# Create your models here.
#implementar as tabelas StatusSenha, Categoria, Tipo e Senha,
# assim como os seus relacionamentos.

class StatusSenha(models.Model):

    id_status_senha = models.IntegerField(max_length=10, null=False, primary_key=True)
    nome = models.CharField(max_length=45)

class Categoria(models.Model):

    id_categoria = models.IntegerField(max_length=10, null=False, primary_key=True)
    nome = models.CharField(max_length=45)


class Tipo(models.Model):

    id_tipo = models.IntegerField(max_length=10, null=False, primary_key=True)
    nome = models.CharField(max_length=45)

class Senha(models.Model):

    id_senha = models.IntegerField(max_length=10, null=False, primary_key=True)
    senha = models.IntegerField(max_length=40, null=False)
    hora_data = models.DateTimeField(auto_now_add=True)

    Categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Tipo_id = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    StatusSenha_id = models.ForeignKey(StatusSenha, on_delete=models.CASCADE)