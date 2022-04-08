from django.db import models
from django.urls import reverse

""" models.py служит для формирование нужной таблице в базе данных  """

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    # определения внешнего ключа для связи с классом class Category
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    # функция для формирования ссылки для постов
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

""" организация связи один ко многим """
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    # функция для формирования ссылки для категорий
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Phones(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})