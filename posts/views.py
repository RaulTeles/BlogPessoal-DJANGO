from django.shortcuts import render, redirect
#importano classe, para criar classe View
from django.views.generic.list import ListView
#importando classe, para editar detalhes do post
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When
#importando a classe Forcomentario do app comentarios
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from django.contrib import messages


class PostIndex(ListView):
    #Sobrescrevendo o model para Post ja criado
    model = Post
    #definindo o template ja criado
    template_name = 'posts/index.html'
    #definindo a paginação
    paginate_by = 4
    #Sobrescrevendo o nome do objeto para ser usando o for no index.html
    context_object_name = 'posts'
    #Sobrescrevendo o metodo queryset para definir a ordem que sera mostrado os posts
    #fazendo filtragem dos commentarios e posts publicados para serem exibidos
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True)

        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True,then=1)
                )
            )
        )
        return qs

class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            Q(titulo_post__icontains=termo) | 
            Q(autor_post__first_name__iexact=termo) | 
            Q(conteudo_post__icontains=termo) | 
            Q(excerto_post__icontains=termo) | 
            Q(categoria_post__nome_cat__iexact=termo)
            
        )
        return qs

class PostCategoria(PostIndex):
    #sobrescrevendo o template name novamente
    template_name = 'posts/post_categoria.html'
    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.kwargs.get('categoria', None)
        if not categoria:
            return qs
        #busca o nome do post para ser filtrado
        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)

        return qs

#update view espera um formulário
class PostDetalhes(UpdateView):
    
    template_name = 'posts/post_detalhes.html'
    model = Post
    context_object_name = 'post'
    form_class = FormComentario


    #Redirenciar cada comentario para o sua categoria e separar os publicados dos nao publicados
    #sobrescrever o metodo get_context_data
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        #pegando qual post estamos
        post = self.get_object()
        #Selecionando comentarios da base de dados
        comentarios = Comentario.objects.filter(publicado_comentario=True,post_comentario=post.id)

        contexto['comentarios'] = comentarios

        return contexto

    #redefinindo o metodo
    def form_valid(self,form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post
        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user
            #salvando comentario
            comentario.save()
            #mensagem de comentario enviado
            messages.success(self.request,'Comentário enviado com Sucesso!')
            #Redirecionando apos enviar o comentario
            return redirect('post_detalhes', pk=post.id)