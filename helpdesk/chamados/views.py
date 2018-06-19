from django.shortcuts import render, redirect
from .models import *
from .Forms import *

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def index(request):
    return render(request, 'index.html', context={})

@login_required
def meus_chamados(request):
    chamados = Chamado.objects.filter(criado_por__usuario=request.user)
    return render(request, 'lista_chamados.html', context={'chamado': chamados})


def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('usuario'), password=request.POST.get('senha'))
        if user is not None:
            login(request, user)
            return redirect('/index.html')

    return render(request, 'login.html')

@login_required
def lista_status(request):
    lista_status = StatusChamado.objects.all()
    return render(request, 'lista_status.html', context={'lista_status':lista_status})

@login_required
def create_status(request):
    return render(request, 'status_add.html', context=None)

@login_required
def salvar_status(request):
    titulo = request.POST.get('nome_status')
    id_status = request.POST.get('id_status')
    
    if id_status:
        status = StatusChamado.objects.get(pk=id_status)
    else:
        status = StatusChamado()
    
    status.titulo = titulo
    status.save()
    return redirect('/status')

@login_required
def edit_status(request, id):
    status = StatusChamado.objects.get(pk=id)
    return render(request, 'status_add.html', context={'status': status})

#######CRUD CATEGORIA##############
@login_required
def list_categoria(request):
    categoria = Categoria.objects.all()
    return render(request, 'list_categoria.html', {'categoria': categoria})

@login_required
def create_categoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/listcategoria/')

    return render(request, 'categoria_form.html', {'form': form})

@login_required
def update_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('/listcategoria/')

    return render(request, 'categoria_form.html', {'form': form, 'categoria': categoria})

@login_required
def delete_categoria(request, id):
    categoria = Categoria.objects.get(pk = id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('/listcategoria/')

    return render(request, 'confirm_delete.html', {'categoria': categoria})

####################Chamados########
@login_required
def newChamado(request):
    form = ChamadoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/chamados/')

    return render(request, 'chamado_form.html', {'form': form})

@login_required
def atendeChamado(request,id):

    chamado = Chamado.objects.get(pk=id)

