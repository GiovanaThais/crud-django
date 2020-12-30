from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView, DeleteView 
from .models import Cliente
from .models import Endereco
from django.urls import reverse_lazy


# Create your views here.
class ClienteList(ListView):
    model = Cliente

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['user','id','cpf','rg','telefone','email']
    success_url = reverse_lazy('cliente_list')

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['user','id','cpf','rg','telefone','email']
    success_url = reverse_lazy('cliente_list')

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')

class EnderecoList(ListView):
    model = Endereco
class EnderecoCreate(CreateView):
    model = Endereco
    fields = ['user','logradouro','bairro','cidade','estado','numero','email']
    success_url = reverse_lazy('endereco_list')

class EnderecoUpdate(UpdateView):
    model = Endereco
    fields = ['user','logradouro','bairro','cidade','estado','numero','email']
    success_url = reverse_lazy('endereco_list')

class EnderecoDelete(DeleteView):
    model = Endereco
    success_url = reverse_lazy('endereco_list')
