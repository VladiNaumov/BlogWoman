import sqlite3

""" пример программы, которая создает новую базу данных перед открытием ее для операций: """

db_filename = '../website/orders.db'
connection = sqlite3.connect(db_filename)
cur = connection.cursor()

""" создание таблице user """
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
connection.commit()

""" заполнаяем таблицу """
cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
   VALUES('00090', 'Alex', 'Smith', 'male');""")
connection.commit()

connection.close()



"""
from blogWoman.models import Women

demo = 'python manage.py shell'

w1 = Women.objects.create(title='Мерил Стрип', content=' ')
w2 = Women.objects.create(title='Сьюзен Сарандон', content=' ')
w3 = Women.objects.create(title='Дайан Китон', content=' ')
w4 = Women.objects.create(title='Джейн Фонда', content=' ')
w5 = Women.objects.create(title='Барбра Стрейзанд', content=' ')
w6 = Women.objects.create(title='Джоди Фостер', content=' ')
w7 = Women.objects.create(title='Джиллиан Андерсон', content=' ')
w8 = Women.objects.create(title='Лора Дерн', content=' ')
w9 = Women.objects.create(title='Скарлетт Йоханссон', content=' ')
w10 = Women.objects.create(title='Дженнифер Энистон', content=' ')


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


from naumdeveloper.models import Naumdeveloper
w0 = Naumdeveloper.objects.create(title='Creating websites', content='Hello, I create websites:')

"""

