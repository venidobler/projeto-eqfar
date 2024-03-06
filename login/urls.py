from django.urls import path
from login import views





urlpatterns = [
    path('', views.login_view, name="login"),
    path('registro/', views.registro, name="registro"),
    path('logout/', views.user_logout, name='user_logout'),
 
   

]

