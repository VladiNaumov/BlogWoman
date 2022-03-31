# Blog Women
# Blog Naumdeveloper


Django


pip install django
django-admin startproject mysite
cd mysite
python manage.py migrate
python manage.py runserver
python manage.py startapp blog
python manage.py makemigrations blog
python manage.py migrate
python manage.py createsuperuser


DB
from blogWoman.models import Phones
Phones(title='Iphone', content='apple Phone')
w1=_
w1
w1.save()

w4 = Phones.objects.create(title='Samsung', content='Samsung Edg 7')
w5 = Phones.objects.create(title='Samsung', content='Samsung A52')
w6 = Phones.objects.create(title='Samsung', content='Samsung S22')
w7 = Phones.objects.create(title='Phone', content='Phone7')
w8 = Phones.objects.create(title='DELL', content='Dell Ti100') 