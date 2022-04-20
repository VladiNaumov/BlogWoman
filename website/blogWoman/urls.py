from django.urls import path
from .views import index, about, phones, addpage, contact, login, show_post, show_category

""" Менеджер URL-ов """

urlpatterns = [
    path('', index, name = 'home'), # http://127.0.0.1:8000/
    path('about/', about, name = 'about'), #http://127.0.0.1:8000/about
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),

    path('phones/', phones, name='phones'),
]

