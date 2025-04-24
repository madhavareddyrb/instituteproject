"""
URL configuration for project project.

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
from django.urls import path
from projectapp import views
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainpage, name= 'mainpage'),
    path('mainpage/',views.mainpage, name='mainpage'),
    path("home/", views.home,name="home"),
    path('services/', views.services,name="services"),
    path('contact/',views.contact,name='contact'),
    path('feedback/',views.feedback,name='feedback'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/success/',views.contact_success,name='contact_success'),
    path("register/",views.register_view , name = "register"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("registraion_success/",views.registraion_success,name="registraion_success"),
    path('feedback/update/<int:pk>/', views.update_feedback, name='feedback_update'),
    path('feedback/delete/<int:pk>/', views.delete_feedback, name='feedback_delete'),
]