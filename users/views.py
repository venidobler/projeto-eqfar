from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cadastro (request):
    return render(request, 'cadastro_usuario.html')

def listagem (request):
    return render(request, 'listagem_usuario.html')