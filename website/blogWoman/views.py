from django.http import HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render

from blogWoman.models import Women, Phones, Category

""" Основное базовое представление на основе класса. 
Все остальные представления, основанные на классах, наследуются от этого базового класса. 
Он не является строго общим представлением и поэтому может быть импортирован из django.views """

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats' : cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
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


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()


    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)

