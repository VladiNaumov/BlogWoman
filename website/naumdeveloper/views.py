from django.http import HttpResponseNotFound
from django.shortcuts import render

from naumdeveloper.models import Naumdeveloper, Stores

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Naumdeveloper.objects.all()
    return render(request, 'naumdeveloper/index.html', {'posts': posts, 'menu': menu, 'title': 'index page'})


def store(request):
    posts = Stores.objects.all()
    return render(request, 'naumdeveloper/store.html', {'posts': posts, 'menu': menu, 'title': 'Store'})

def email(request):
    return render(request, 'naumdeveloper/email.html', {'menu': menu, 'title': 'email'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
