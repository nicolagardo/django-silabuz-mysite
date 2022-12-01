"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from escuela.views import (
    index_view,
    index_view2,
    IndexView,
    index_view3,
    IndexView2,
    IndexViewWithContex,
    IndexViewWithContex2,
    form_index,
    form_alum,
    alumD)

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("login/", admin.site.urls)
    path("home", index_view2, name="home"),
    path("home2", IndexView.as_view()),
    path("home3", index_view3),
    path("home4", IndexView2.as_view()),
    path("home5", IndexViewWithContex.as_view()),
    path("solucion2", IndexViewWithContex2.as_view()),
    path("forms1", form_index),






    path("formAlum", form_alum, name="formAlum"),
    path("formAlum/<alum>", alumD, name="alum", ),

]
