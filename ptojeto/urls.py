"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from equipments import views
from users import views
from home import views
from login import views
from products import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from gantt.views import index

urlpatterns = [
     
    path('home/', include('home.urls')),
    path('cadastro_usuario/',include('users.urls')),
    path('cadastro_equipamento/',include('equipments.urls')),
    path('cadastro_produto/', include('products.urls')),
    path('', include('login.urls')),
    path('admin/', admin.site.urls),
    path('index/', index),
    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

