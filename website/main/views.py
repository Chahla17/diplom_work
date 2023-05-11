from django.shortcuts import render, redirect
from .forms import TaskForm, RegistrationForm
from django.contrib.auth import login, logout, authenticate

def index(request):
    return render(request, 'main/index.html',)


def about(request):
    return render(request, 'main/menu.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заказа была не верной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/bar.html', context)


def book(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заказа была не верной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/book.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    else:
        form = RegistrationForm()

    args = {'form': form}

    return render(request, 'registration/sign_up.html', args)