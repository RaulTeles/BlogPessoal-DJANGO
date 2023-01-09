from django.urls import path
from . import views

#Os views, precisam ser callable, pelo fato de usar as classes ex: .PostIndex.as_view()

urlpatterns = [
     #url principal do posts, HOME DO SITE
    path('', views.PostIndex.as_view(), name='index'),
     #url para categoria, Recebe uma string "categoria"
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post_categoria'),
    #busca nao recebe nada, pois será via GET
    path('busca/', views.PostBusca.as_view(), name='post_busca'), 
    #url para detalhes, receben um <int:pk>, poderia ser <int:id>
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'), 
]