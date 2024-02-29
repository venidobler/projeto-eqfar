from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm, ProdutoEditForm

def home_produto(request):
    return render(request, 'home/home_produto.html')

def cadastro_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_produto')
    else:
        form = ProdutoForm()

    return render(request, 'produtos/cadastro_produto.html', {'form': form})

def listagem_produto(request):
    produtos = {
        'produtos': Produto.objects.all().order_by('id_produto')
    }
    return render(request, 'produtos/listagem_produto.html', produtos)

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id_produto=produto_id)

    if request.method == 'POST':
        form = ProdutoEditForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listagem_produto')
    else:
        form = ProdutoEditForm(instance=produto)

    return render(request, 'produtos/editar_produto.html', {'form': form, 'produto_id': produto_id})

def delete_product(request, produto_id):
    usuario = get_object_or_404(Produto, pk=produto_id)
    usuario.delete()
    return redirect('listagem_produto')