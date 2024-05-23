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
    path('delete_equipment/<int:equipamento_id>/',views.delete_equipment, name='delete_equipment'),
]
