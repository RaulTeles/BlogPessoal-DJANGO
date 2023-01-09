from django.db import models
#importando o models do startapp categorias
from categorias.models import Categoria
#importando a classe usuario (autor)
from django.contrib.auth.models import User
#importando as configurações da data
from django.utils import timezone




#Configurando a base de dados
class Post(models.Model):
    #Verbose_name é para auterar o nome da barra admin
    titulo_post = models.CharField(max_length=255, verbose_name='Titulo')
    #O User on_delete, é se caso o usuario for deletado, não acontecer nada
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteudo')
    excerto_post = models.TextField(verbose_name='Excerto')
    #deixar um post sem categoria
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank= True, null=True, verbose_name='Categoria')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.titulo_post