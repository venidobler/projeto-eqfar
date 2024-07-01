from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def acessar_admin(request):
  return redirect('admin:index')


# Create your views here.
def home (request):
    return render(request, 'pages/home.html')