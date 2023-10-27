from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

# Create your views here.

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produtos/lista.html'
    context_object_name = 'produtos'

class DetalheProdutos(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('DetalheProdutos')

class AdicionarAoCarrinho(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('AdicionarAoCarrinho')

class RemoverDoCarrinho(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('RemoverDoCarrinho')

class Carrinho(View):
    def get(Self,*args, **kwargs):
            return HttpResponse('Carrinho')
    
class Finalizar(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('Finalizar')