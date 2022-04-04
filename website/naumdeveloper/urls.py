from django.urls import path

from naumdeveloper.views import index, store, email

urlpatterns = [
    path('', index, name = 'home'), # http://127.0.0.1:8000/naumdeveloper
    path('email/', email, name = 'email'), # http://127.0.0.1:8000/naumdeveloper/email
    path('store/', store, name = 'store' )
]

