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
from equipments import views


urlpatterns = [
    path('', views.home_equipamento, name="home_equipamento"),
    # equipamentos.com/cadastro
    path('cadastro/', views.cadastro_equipamento, name="cadastro_equipamento"),
    # equipamentos.com/listagem_cliente
    path('listagem_equipamento/', views.listagem_equipamento, name='listagem_equipamento'),
    # equipamentos.com/editar
    path('editar/<int:equipamento_id>/', views.editar_equipamento, name="editar_equipamento"),
    # equipamentos.com/excluir
    path('delete_user/<int:equipamento_id>/',views.delete_equipment, name='delete_equipment'),
]
