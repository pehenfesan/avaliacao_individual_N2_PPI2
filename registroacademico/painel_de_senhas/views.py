from django.shortcuts import render

from django.http import HttpResponse

from painel_de_senhas.models import StatusSenha, Tipo, Senha, Categoria

def index(request):
    #senhasTot = Senha.objects.get(StatusSenha_id.nome='Na fila')    
    
    return render(request, 'index.html',{'senhas' : Senha.objects.all()})