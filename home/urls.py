from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('acessar_admin/', views.acessar_admin, name='acessar_admin'),
]
