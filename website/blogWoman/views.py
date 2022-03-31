from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from blogWoman.models import Women, Phones

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'index page'})


def phones(request):
    posts = Phones.objects.all()
    return render(request, 'women/store.html', {'posts': posts, 'menu': menu, 'title': 'Phones'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Abaut'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')