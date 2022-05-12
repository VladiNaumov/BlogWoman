from django.http import HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from blogWoman.forms import AddPostForm
from blogWoman.models import Women,Category


""" Основное базовое представление на основе класса. 
Все остальные представления, основанные на классах, наследуются от этого базового класса. 
Он не является строго общим представлением и поэтому может быть импортирован из django.views """

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
""" class - отвечает за главную страницу сайта """
class WomenHome(ListView):
    # выбирает все записи из таблице BD Woman
    model = Women
    # подключение данной странице ('index.html') к шаблонизатору
    template_name = 'women/index.html'
    # указываем какую переменную в Менеджер URL-ов url.py мы используем
    context_object_name = 'posts'

    """ 
    метод get_context_data объединяет(сливает вместе) данные контекста всех родительских классов с данными текущего класса. 
    Чтобы сохранить такое поведение в пользовательских классах, в которых вы собираетесь изменять контекст, 
    вы должны в начале вызвать метод get_context_data родительского класса.
    Также вы може написать свои ORM-запросы к базе....
    Если нет двух классов, которые пытаются определить одинаковый ключ - вы получите желаемый результат. 
    Однако, если есть некий класс, который пытается переопределить ключ, установленный родительскими классами(после вызова super), то любой потомок этого класса также должен явно установить такой ключ(после вызова super), если необходимо гарантировать полное переопределение данных родителей. 
    Если у вас возникли проблемы, просмотрите mro(method resolution order) вашего представления. 
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0

        return context

    # данный метод чтобы говорить Django,что именно мы хотим отображать на странице сайта
    def get_queryset(self):
        # чтобы читать только опубликованные статьи
        return Women.objects.filter(is_published=True)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Abaut'})

""" class для работы с формами """
class AddPage(CreateView):
    form_class = AddPostForm

    # подключение данной странице 'addpage.html' к шаблонизатору
    template_name = 'women/addpage.html'

    # указываем какую переменную в Менеджер URL-ов url.py мы используем
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context


def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

# class для работы (показа) поста
class ShowPost(DetailView):
    # выбирает все записи из таблице BD Woman
    model = Women

    # подключение данной странице ('post.html') к шаблонизатору
    template_name = 'women/post.html'

    # указываем какую переменную в Менеджер URL-ов url.py мы используем
    slug_url_kwarg = 'post_slug'

    # указываем какую переменную в Менеджер URL-ов url.py мы используем
    context_object_name = 'post'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    # отработка странице 404
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context


