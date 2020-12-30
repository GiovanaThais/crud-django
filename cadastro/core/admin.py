from django.contrib import admin
from .models import Cliente
from .models import Endereco
# Register your models here.
#admin.site.register(Cliente)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id','foto','cpf','rg','telefone','email']

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['cidade','estado','logradouro','bairro','numero','email']