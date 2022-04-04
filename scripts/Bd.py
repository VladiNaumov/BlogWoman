import sqlite3

""" пример программы, которая создает новую базу данных перед открытием ее для операций: """

db_filename = '../website/orders.db'
#db_filename = '../website/db.sqlite3'
connection = sqlite3.connect(db_filename)
cur = connection.cursor()

""" создание таблице user """
#cur.execute("""CREATE TABLE IF NOT EXISTS users(
#   userid INT PRIMARY KEY,
#   fname TEXT,
#   lname TEXT,
#   gender TEXT);
#""")
#connection.commit()

""" заполнаяем таблицу """
#cur.execute("""INSERT INTO users(userid, fname, lname, gender)
#   VALUES('00090', 'Alex', 'Smith', 'male');""")
#connection.commit()

#more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce', 'Wayne', 'male')]

"""
customers = [
  ('00005', 'Stephanie', 'Stewart', 'female'), ('00006', 'Sincere', 'Sherman', 'female'), ('00007', 'Sidney', 'Horn', 'male'),
  ('00008', 'Litzy', 'Yates', 'female'), ('00009', 'Jaxon', 'Mills', 'male'), ('00010', 'Paul', 'Richard', 'male'),
  ('00011', 'Kamari', 'Holden', 'female'), ('00012', 'Gaige', 'Summers', 'female'), ('00013', 'Andrea', 'Snow', 'female'),
  ('00014', 'Angelica', 'Barnes', 'female'), ('00015', 'Leah', 'Pitts', 'female'), ('00016', 'Dillan', 'Olsen', 'male'),
  ('00017', 'Joe', 'Walsh', 'male'), ('00018', 'Reagan', 'Cooper', 'male'), ('00019', 'Aubree', 'Hogan', 'female'),
  ('00020', 'Avery', 'Floyd', 'male'), ('00021', 'Elianna', 'Simmons', 'female'), ('00022', 'Rodney', 'Stout', 'male'),
  ('00023', 'Elaine', 'Mcintosh', 'female'), ('00024', 'Myla', 'Mckenzie', 'female'), ('00025', 'Alijah', 'Horn', 'female'),
  ('00026', 'Rohan', 'Peterson', 'male'), ('00027', 'Irene', 'Walters', 'female'), ('00028', 'Lilia', 'Sellers', 'female'),
  ('00029', 'Perla', 'Jefferson', 'female'), ('00030', 'Ashley', 'Klein', 'female')
]

cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", customers)
connection.commit()
"""

""" Получение данных с SQLite в Python """

"""
cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
print(one_result)

# скрипт для генерации 3 результатов
cur.execute("SELECT * FROM users;")
three_results = cur.fetchmany(3)
print(three_results)


"""

# Функцию fetchall() можно использовать для получения всех результатов.
cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
print(all_results)

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

