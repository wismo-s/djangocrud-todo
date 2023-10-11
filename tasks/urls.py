from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('singup/', views.singup, name='singup'),
    path('tasks/', views.tasks, name='tasks'),
    path('logout/', views.singout, name='logout'),
    path('login/', views.lognin, name='lognin'),
    path('tasks/create/', views.createTask, name='createTaks')
]
