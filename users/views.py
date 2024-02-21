from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm, UsuarioEditForm

def home_usuario(request):
    return render(request, 'home/home_usuario.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_usuario')
    else:
        form = UsuarioForm()

    return render(request, 'usuarios/cadastro_usuario.html', {'form': form})

def listagem_usuario(request):
    usuarios = {
        'usuarios': Usuario.objects.all().order_by('id_usuario')
    }
    return render(request, 'usuarios/listagem_usuario.html', usuarios)

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)

    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listagem_usuario')
    else:
        form = UsuarioEditForm(instance=usuario)

    return render(request, 'usuarios/editar_usuario.html', {'form': form, 'usuario_id': usuario_id})

def delete_user(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    usuario.delete()
    return redirect('listagem_usuario')