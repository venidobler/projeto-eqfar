from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cadastro (request):
    return render(request, 'cadastro_equipamento.html')

def listagem (request):
    return render(request, 'listagem_equipamento.html')