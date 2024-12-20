"""
URL configuration for apoo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from home import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/', views.home),
    path('formulario/doador/', views.formulario_doador, name='formulario_doador'),
    path('formulario/criador/', views.formulario_criador, name='formulario_campanha'),
    path('formulario/estabelecimento/', views.formulario_estabelecimento, name='formulario_estabelecimento'),
    path('perfil_criador/<int:criador_id>/', views.perfil_criador, name='perfil_criador'),
    path('criar_campanha/<int:criador_id>/', views.criar_campanha, name='criar_campanha'),
    path("select2/", include("django_select2.urls")),
    path('login/', views.login_criador, name='login_criador'),
    path('logout/', views.logout_criador, name='logout_criador'),
    path('sucesso_campanha/<int:criador_id>/', views.sucesso_campanha, name='sucesso_campanha'),
    path('sucesso', views.sucesso, name='sucesso')
]
