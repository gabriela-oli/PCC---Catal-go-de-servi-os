from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from produto.forms import ProdutoForm
from .models import Produto
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    produto = Produto.objects.all()
    context = {
        'produtos': produto,
    }
    return render(request, 'produto/listar.html', context)

@login_required
def detail(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    
    context = {
        'produto' : produto
    }
    
    return render(request, 'produto/detail.html', context)

@login_required
def excluir(request, produto_id):
    
    Produto.objects.get(pk=produto_id).delete()
    
    return HttpResponseRedirect("/produto")

@login_required
def criar(request):
    
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/produto")
    else:
        form = ProdutoForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'produto/formCriar.html', context)

@login_required
def editar(request, produto_id):
    
    produto = Produto.objects.get(id=produto_id)
    
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/produto")
    else:
        form = ProdutoForm(instance=produto)
    
    context = {
        'form': form,
        'produto_id': produto_id
    }
    
    
    return render(request, 'produto/editForm.html', context)

def base(request):
    return render(request,'base.html')
