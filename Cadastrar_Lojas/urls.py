from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('Cadastrar_Lojas/Categoria', views.CategoriaList.as_view()),
    path('Cadastrar_Lojas/Categoria/<int:pk>/', views.CategoriaDetail.as_view()),
    path('Cadastrar_Lojas/Loja', views.LojaList.as_view()),
    path('Cadastrar_Lojas/Loja/<int:pk>/', views.LojaDetail.as_view()),
#    path('Cadastrar_Lojas/Produto', views.ProdutoList.as_view()),
#    path('Cadastrar_Lojas/Produto/<int:pk>/', views.ProdutoDetail.as_view()),
#    path('Cadastrar_Lojas/Promocao', views.PromocaoList.as_view()),
#    path('Cadastrar_Lojas/Promocao/<int:pk>/', views.PromocaoDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)