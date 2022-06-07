from ast import Index
from django import views
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.IndexView.as_view(), name='home'),
    path('sobre',views.SobreView.as_view(), name='sobre'),
    path('empresas',views.ProdutosView.as_view(), name='empresas'),
    path('locais',views.LocaisView.as_view(), name='locais'),
    path('contato',views.IndexView.as_view(), name='contato'),
    path('cadastro/cidade',views.cadastro_cidade, name='cidade'),
    path('cadastro/empresa',views.cadastro_empresa, name='empresa'),
    path('cadastro/local',views.cadastro_local, name='local'),
    path('cadastro/produto',views.cadastro_produto, name='produto'),
    path('painel',views.painel, name='painel'),
    path('listar/cidade',views.list_cidade, name='list_cidade'),
    path('listar/cidade/<id>',views.expandir_cidade, name='expandir_cidade'),
    path('listar/cidade/<id>/excluir',views.excluir_cidade, name='excluir_cidade'),
    path('listar/empresa',views.list_empresa, name='list_empresa'),
    path('listar/empresa/<id>',views.expandir_empresa, name='expandir_empresa'),
    path('listar/empresa/<id>/excluir',views.excluir_empresa, name='excluir_empresa'),
    path('listar/empresa/<id>/editar',views.alterar_empresa, name='alterar_empresa'),
    path('listar/produto',views.list_produto, name='list_produto'),
    path('listar/produto/<id>',views.expandir_produto, name='expandir_produto'),
    path('listar/produto/<id>/excluir',views.excluir_produto, name='excluir_produto'),
    path('listar/produto/<id>/editar',views.alterar_produto, name='alterar_produto'),
]
