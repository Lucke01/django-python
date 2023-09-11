"""
URL configuration for ProyectoIntroductorio project.

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
from django.contrib import admin
from django.urls import path
from ProyectoIntroductorio.view import saludo,segunda_vista,diahoy,Mi_nombre,probandoTemplate,Template_Mejorado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('vista_2/', segunda_vista),
    path('hoy/',diahoy),
    path('MeLlamo/<nombre>', Mi_nombre),
    path('template/',probandoTemplate ),
    path('template_mejorado/', Template_Mejorado),
]
