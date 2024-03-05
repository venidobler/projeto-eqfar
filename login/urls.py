from django.urls import path
from login import views




urlpatterns = [
    path('', views.login, name="login"),
    path('registro/', views.registro, name="registro"),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.user_profile, name='user_profile'),

]

