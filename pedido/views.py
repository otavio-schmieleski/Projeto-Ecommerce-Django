from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


# Create your views here.
class Pagar(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('Pagar')

class SalvarPedido(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('FecharPedido')

class Detalhe(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('Detalhe')