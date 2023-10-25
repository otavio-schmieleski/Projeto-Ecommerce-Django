from django.contrib import admin
from . import models

# criando variacao do tipo tabela e atribuindo uma linha extra
class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1

# montando os produtos com a variacao na parte inferior
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]


# Register your models here.
admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)