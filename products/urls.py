"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from products import views


urlpatterns = [
    path('', views.home_produto, name="home_produto"),
    # produtos.com/cadastro
    path('cadastro/', views.cadastro_produto, name="cadastro_produto"),
    # produtos.com/listagem_cliente
    path('listagem_produto/', views.listagem_produto, name='listagem_produto'),
    # produtos.com/editar
    path('editar/<int:produto_id>/', views.editar_produto, name="editar_produto"),
    # produtos.com/excluir
    path('delete_product/<int:produto_id>/',views.delete_product, name='delete_product'),
]