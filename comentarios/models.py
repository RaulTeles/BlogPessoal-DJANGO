from django.db import models
#importando o post
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='Email')
    comentario = models.TextField(verbose_name='Comentário')
    #Quando o post for eliminado, irá apagar todos os comentarios
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_comentario = models.DateTimeField(default=timezone.now)
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    publicado_comentario = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_comentario