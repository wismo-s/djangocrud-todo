from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('singup/', views.singup, name='singup'),
    path('tasks/', views.tasks, name='tasks'),
    path('logout/', views.singout, name='logout'),
    path('login/', views.lognin, name='lognin'),
    path('tasks/create/', views.createTask, name='createTaks'),
    path('tasks/<int:task_id>/', views.tasksdetail, name='taksDetail'),
    path('tasks/<int:task_id>/complete', views.completetask, name='taksCompleted'),
    path('tasks/<int:task_id>/delete', views.deletetask, name='taksDelete'),
    path('tasks/completed', views.listcompletetask, name='listcompletetask')
]
