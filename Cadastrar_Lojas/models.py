from django.db import models
from django.utils import timezone

class Loja(models.Model):
    loja = models.CharField(max_length=120)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=2)
    email = models.CharField(max_length=200) 

    class Meta:
        verbose_name = ("Loja")
        verbose_name_plural = ("Lojas")
    
    def __str__(self):
        return self.loja #retorna o nome da loja

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)    
    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.categoria

class Produto(models.Model):
    produto = models.CharField(max_length=120)
    imagem = models.CharField(max_length=255) #link de uma imagem online  
    descricao = models.TextField(blank=True)    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)   
    
    def __str__(self):
        return self.produto #retorna o nome do produto

class Promocao(models.Model):
    promo = models.ForeignKey(Produto, on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    preco = models.CharField(max_length=10)
    cupom = models.CharField(max_length=20)
    destaque = models.BooleanField() 
        
    def __str__(self):
        return self.cupom #retorna o nome do produto na promocao