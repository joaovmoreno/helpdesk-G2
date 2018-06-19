from django.forms import ModelForm
from .models import *

class CategoriaForm(ModelForm):
    class Meta():
        model = Categoria
        fields = ['titulo']

class ChamadoForm(ModelForm):

    class Meta():
        model = Chamado
        fields = ['titulo','descricao','categoria','telefone','data_abertura','status','criado_por']