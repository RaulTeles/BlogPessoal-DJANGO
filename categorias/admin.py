from django.contrib import admin
from . models import Categoria

#herdando o models

class CategoriaAdmin(admin.ModelAdmin):
    #Definindo quais categorias, queremos exibir
    list_display = ('id', 'nome_cat')
    #nomes para clicar la categoria
    list_display_links = ('id', 'nome_cat')

#Registrando a classe Categoria e CategoriaAdmin
admin.site.register(Categoria, CategoriaAdmin)