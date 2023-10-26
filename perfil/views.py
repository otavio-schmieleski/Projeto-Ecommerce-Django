from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Criar(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('Criar')

class Atualizar(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('Atualizar')

class Login(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('Login')

class Logout(View):
    def get(Self,*args, **kwargs):
        return HttpResponse('Logout')
