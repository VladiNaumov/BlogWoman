from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'index page'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Abaut'})

def phones(request):
    return HttpResponse('<h1>PHONES</h1>')

def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=False) # permanent=False->redirect 302, permanent=True -> 301

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')