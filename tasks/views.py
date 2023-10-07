from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def singup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create(username = request.POST['username'], password = request.POST['password1'])
                user.save()
                return redirect('singupdone')
            except:
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

def singupdone(request):
    return render(request, 'singupdone.html')