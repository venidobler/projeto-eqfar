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
from users import views


urlpatterns = [
    path('', views.home_usuario, name="home_usuario"),
    # usuarios.com/cadastro
    path('cadastro/', views.cadastro_usuario, name="cadastro_usuario"),
    # usuarios.com/listagem_cliente
    path('listagem_usuario/', views.listagem_usuario, name='listagem_usuario'),
    # usuarios.com/editar
    path('editar/<int:usuario_id>/', views.editar_usuario, name="editar_usuario"),
    # usuarios.com/excluir
    path('delete_user/<int:usuario_id>/',views.delete_user, name='delete_user'),
]
