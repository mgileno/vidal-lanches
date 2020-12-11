from django.contrib import admin
from .models import Categoria, Loja, Produto, Promocao

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("categoria",)

class LojaAdmin(admin.ModelAdmin):
    list_display = ("loja",)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("produto",)

class PromocaoAdmin(admin.ModelAdmin):
    list_display = ("promo",)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Loja, LojaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Promocao, PromocaoAdmin)
