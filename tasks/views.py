from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def singup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create(username = request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    'error': 'el usuario ya existe'
                })
        else:
            return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    'error': 'no conicide las contrasenas'
                })
    else:
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })

def tasks(request):
    return render(request, 'tasks.html')

def singout(request):
    logout(request)
    return redirect('singup')

def lognin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')

def createTask(request):
    if request.method == 'GET':
        return render(request, 'create_taks.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            print(new_task)
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_taks.html', {
                'form': TaskForm,
                'error': "pase un dato correcto"
            })