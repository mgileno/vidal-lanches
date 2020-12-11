from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('Cadastrar_Lojas/Categoria', views.CategoriaList.as_view()),
    path('Cadastrar_Lojas/Categoria/<int:pk>', views.CategoriaDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)