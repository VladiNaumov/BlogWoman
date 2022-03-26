from django.urls import path, re_path
from .views import index, categories, archive, about

urlpatterns = [
    path('', index, name = 'home'), # http://127.0.0.1:8000/
    path('about/', about, name = 'about')
]

