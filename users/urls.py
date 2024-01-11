from django.urls import path

from users.views import cadastro, listagem


urlpatterns = [
 
    path('cadastro/', cadastro),
    path('listagem/', listagem),

]