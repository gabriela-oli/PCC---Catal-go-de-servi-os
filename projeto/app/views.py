from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Cidade,Local,Produto,Empresa
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)

class IndexView(TemplateView):
    template_name = 'index.html'


class SobreView(TemplateView):
    template_name = 'about.html'
    
class LocaisView(TemplateView):
    template_name = 'portfolio.html'
    
class ProdutosView(TemplateView):
    template_name = 'service.html'

def cadastro_cidade(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cidade = Cidade()
        cidade = Cidade.objects.create(nome=nome)


    return render(request, 'cadastro.html')

def cadastro_empresa(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        cidade_name = request.POST.get('cidade_name') 
        empresa = Empresa.objects.create(nome=nome, endereco=endereco,cidade_name=cidade_name)

    cidade = Cidade.objects.all()

    return render(request, 'cadastro-empresa.html', {'cidades': cidade})


def cadastro_local(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        cidade_name = request.POST.get('cidade_name') 
        local = Local.objects.create(nome=nome, descricao=descricao,cidade_name=cidade_name)

    cidade = Cidade.objects.all()

    return render(request, 'cadastro-local.html', {'cidades': cidade})


def cadastro_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        contato = request.POST.get('contato')
        empresa = request.POST.get('empresa') 
        produto = Produto.objects.create(nome=nome, descricao=descricao,contato=contato,empresa=empresa)

    empresa = Empresa.objects.all()

    return render(request, 'cadastro-produto.html', {'empresas': empresa})


def painel(request):

    return render(request, 'painel-admin.html')

def list_cidade(request):

    cidade = Cidade.objects.all()
    return render(request, 'listar_cidade.html', {'cidades': cidade})


def expandir_cidade(request, id):

    context ={}
 
    context["cidade"] = Cidade.objects.get(id = id)
         
    return render(request, "mostar-cidade.html", context)    

 


def alterar_cidade(request, id):
    context ={}
    obj = get_object_or_404(Cidade, id = id)

 
    return render(request, "", context)


def excluir_cidade(request, id):
    context ={}
    context["cidade"] = Cidade.objects.get(id = id) 
    obj = get_object_or_404(Cidade, id = id) 
    obj.delete()
    return HttpResponseRedirect("listar/cidade")
 
# ---------------------------------------------------------------------------
# Empresas

def list_empresa(request):

    empresa = Empresa.objects.all()
    return render(request, 'listar_empresa.html', {'empresas': empresa})


def expandir_empresa(request, id):

    context ={}
 
    context["empresa"] = Empresa.objects.get(id = id)
         
    return render(request, "mostar_empresa.html", context)    



def alterar_empresa(request, id):
    obj = get_object_or_404(Empresa, id = id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        cidade_name = request.POST.get('cidade_name') 
        empresa = Empresa.objects.create(nome=nome, endereco=endereco,cidade_name=cidade_name)

    cidade = Cidade.objects.all()

    return render(request, 'alterar-empresa.html', {'cidades': cidade})


def excluir_empresa(request, id):
    context ={}
    context["empresa"] = Empresa.objects.get(id = id) 
    obj = get_object_or_404(Empresa, id = id) 
    obj.delete()
    return HttpResponseRedirect("listar/empresa")
 


# ---------------------------------------------------------------------------
# Produto

def list_produto(request):

    produto = Produto.objects.all()
    return render(request, 'listar_produto.html', {'produtos': produto})


def expandir_produto(request, id):

    context ={}
 
    context["produto"] = Produto.objects.get(id = id)
         
    return render(request, "mostar_produto.html", context)    



def alterar_produto(request, id):
    obj = get_object_or_404(produto, id = id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        cidade_name = request.POST.get('cidade_name') 
        produto = produto.objects.create(nome=nome, endereco=endereco,cidade_name=cidade_name)

    cidade = Cidade.objects.all()

    return render(request, 'alterar-produto.html', {'cidades': cidade})


def excluir_produto(request, id):
    context ={}
    context["produto"] = Produto.objects.get(id = id) 
    obj = get_object_or_404(Produto, id = id) 
    obj.delete()
    return HttpResponseRedirect("listar/produto")
 




