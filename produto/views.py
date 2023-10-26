from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
# Create your views here.

class ListaProdutos(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('ListaProdutos')

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