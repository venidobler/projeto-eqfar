from django.urls import path
from reports.views import relatorio



urlpatterns = [
    path('', relatorio),

]