from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from empresa.forms import EmpresaForm
from .models import Empresa
from django.contrib.auth.decorators import login_required

def template(request):
    
    return render(request, 'index.html', {})


@login_required
def index(request):
    empresa = Empresa.objects.all()
    context = {
        'empresas': empresa,
    }
    return render(request, 'empresa/listar.html', context)

@login_required
def detail(request, empresa_id):
    empresa = Empresa.objects.get(pk=empresa_id)
    
    context = {
        'empresa' : empresa
    }
    
    return render(request, 'empresa/detail.html', context)

@login_required
def excluir(request, empresa_id):
    
    Empresa.objects.get(pk=empresa_id).delete()
    
    return HttpResponseRedirect("/empresa")

@login_required
def criar(request):
    
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/empresa")
    else:
        form = EmpresaForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'empresa/formCriar.html', context)

@login_required
def editar(request, empresa_id):
    
    empresa = Empresa.objects.get(id=empresa_id)
    
    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/empresa")
    else:
        form = EmpresaForm(instance=empresa)
    
    context = {
        'form': form,
        'empresa_id': empresa_id
    }
    
    
    return render(request, 'empresa/editForm.html', context)
