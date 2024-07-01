from django.urls import path
from gantt import views

urlpatterns = [
    path('', views.index, name="index_gantt"),
    path('exportar_relatorio/', views.exportar_relatorio, name="exportar_relatorio"),
    path('relatorio/', views.relatorio, name="relatorio"),
]
