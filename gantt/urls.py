from django.urls import path
from gantt import views

urlpatterns = [
    path('', views.index, name="index_gantt"),
    
]
