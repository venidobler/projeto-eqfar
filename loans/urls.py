from django.urls import path
from . import views

urlpatterns = [
    path('emprestimo/', views.emprestimo_view, name='emprestimo_view'),
    path('devolucao/', views.devolucao_view, name='devolucao_view'),
]


