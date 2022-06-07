from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:produto_id>/', views.detail, name='detail'),
    path('excluir/<int:produto_id>/', views.excluir, name='excluir'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:produto_id>/', views.editar, name='editar'),
]