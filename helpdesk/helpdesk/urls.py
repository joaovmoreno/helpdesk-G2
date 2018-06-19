
from django.contrib import admin
from django.urls import path
from chamados.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticar/', do_login, name='autenticar'),
  #  path('cadastrar/', singup, name = 'singup'),
    path('', index),
    path('chamados/', meus_chamados),
    path('status/', lista_status, name='home_status'),
    path('status/add', create_status, name='create_status'),
    path('status/edit/<int:id>/', edit_status, name='edit_status'),
    path('status/salvar', salvar_status, name='salvar_status'),

    path('newchamado/', newChamado, name='newchamado'),
    path('atendechamado/<int:id>/', atendeChamado, name='atendeChamado'),

    path('listcategoria/', list_categoria, name='list_categoria'),
    path('newcategoria/', create_categoria, name='create_categoria'),
    path('updatecategoria/<int:id>/', update_categoria, name='update_categoria'),
    path('deletecategoria/<int:id>/', delete_categoria, name='delete_categoria'),

]
