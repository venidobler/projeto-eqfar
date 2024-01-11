from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def relatorio (request):
    return render (request, 'relatorio.html')