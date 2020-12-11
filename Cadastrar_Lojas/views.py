from .models import Loja, Produto, Categoria, Promocao
from .serializers import LojaSerializer, ProdutoSerializer, CategoriaSerializer, ProdutoSerializer
from django.http import Http404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CategoriaList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        get_data = request.query_params
        categoria = Categoria.objects.all()
        if 'categoria' in get_data:
            categoria = categoria.filter(categoria=get_data.get('categoria'))        
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class CategoriaDetail(APIView):    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaSerializer(categoria, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LojaList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        get_data = request.query_params
        loja = Loja.objects.all()
        if 'loja' in get_data:
            loja = loja.filter(loja=get_data.get('loja'))        
        serializer = LojaSerializer(loja, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LojaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class LojaDetail(APIView):    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Loja.objects.get(pk=pk)
        except Loja.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        loja = self.get_object(pk)
        serializer = LojaSerializer(loja)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        loja = self.get_object(pk)
        serializer = LojaSerializer(loja, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        loja = self.get_object(pk)
        serializer = LojaSerializer(loja, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        loja = self.get_object(pk)
        loja.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProdutoList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        get_data = request.query_params
        produto = Produto.objects.all()
        if 'produto' in get_data:
            produto = produto.filter(produto=get_data.get('produto'))        
        serializer = ProdutoSerializer(produto, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class ProdutoDetail(APIView):    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Produto.objects.get(pk=pk)
        except Produto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        produto = self.get_object(pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PromocaoList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        get_data = request.query_params
        promocao = Promocao.objects.all()
        if 'promocao' in get_data:
            promocao = promocao.filter(promocao=get_data.get('promocao'))        
        serializer = PromocaoSerializer(promocao, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PromocaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class PromocaoDetail(APIView):    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Promocao.objects.get(pk=pk)
        except Promocao.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        promocao = self.get_object(pk)
        serializer = PromocaoSerializer(promocao)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        promocao = self.get_object(pk)
        serializer = PromocaoSerializer(promocao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        promocao = self.get_object(pk)
        serializer = PromocaoSerializer(promocao, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        promocao = self.get_object(pk)
        promocao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)