from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):

        #Validando formulário, para mostrar cada mensagem de erro nos seus devidos campos
    def clean(self):
        data = self.cleaned_data
        #Pegando as informações do comentario
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais de 5 Caracteres.'
            )
      


    class Meta:
        model = Comentario
        #adicionando o nome dos campos que vai ter nos comentarios
        fields = ('nome_comentario', 'email_comentario', 'comentario')
