from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render

from blogWoman.models import Women, Phones

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'women/index.html', context=context)


def phones(request):
    posts = Phones.objects.all()
    return render(request, 'women/phones.html', {'posts': posts, 'menu': menu, 'title': 'Phones'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Abaut'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')