from .models import Loja, Produto, Promocao, Categoria
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    # permite trazer o campo do objeto e não o ID
    # categoria = serializers.SlugRelatedField(many=False, read_only=False, queryset=Categoria.objects.all(),slug_field='categoria') 
    class Meta:
        model = Categoria
        fields = ['categoria']

class LojaSerializer(serializers.ModelSerializer):   
    # permite trazer o campo do objeto e não o ID
    # Loja = serializers.SlugRelatedField(many=False, read_only=False, queryset=Loja.objects.all(),slug_field='loja') 
    class Meta:
        model = Loja
        fields = ['loja', 'cidade', 'estado', 'email']

class ProdutoSerializer(serializers.ModelSerializer):   
    # permite trazer o campo do objeto e não o ID
    # Produto = serializers.SlugRelatedField(many=False, read_only=False, queryset=Produto.objects.all(),slug_field='produto') 
    class Meta:
        model = Produto
        fields = ['produto', 'imagem', 'descricao', 'categoria']

class PromocaoSerializer(serializers.ModelSerializer):   
    # permite trazer o campo do objeto e não o ID
    # Promocao = serializers.SlugRelatedField(many=False, read_only=False, queryset=Promocao.objects.all(),slug_field='promo') 
    class Meta:
        model = Promocao
        fields = ['promo', 'loja', 'preco', 'cupom','destaque']