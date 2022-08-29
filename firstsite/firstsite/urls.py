"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from pages import views



app_name = 'firstsite'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name="home"),
    path('register/', views.user_create_view, name="createUser"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('newTodo/', views.todo_create_view, name="createTodo"),
    path('deleteTodo/', views.delete_todo, name="deleteTodo"),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.delete_todo, name='todo_delete'),
]
