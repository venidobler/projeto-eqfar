from django.urls import path
from equipments.views import cadastro, listagem

urlpatterns = [   
    path('cadastro/', cadastro),
    path('listagem/', listagem),
   
]