from django.contrib import admin
#importando models do post
from .models import Post
from django_summernote.admin import SummernoteModelAdmin



class PostAdmin(SummernoteModelAdmin):
    #Definindo quais posts queremos exibir
    list_display = ('id','titulo_post','autor_post','data_post','categoria_post','publicado_post',)

    #Configurando para editar o publicado, na lista
    list_editable = ('publicado_post',)
    list_display_links = ('id','titulo_post',)
    summernote_fields = ('conteudo_post',)

#Registrando

admin.site.register(Post, PostAdmin)
X_FRAME_OPTIONS = 'SAMEORIGIN'