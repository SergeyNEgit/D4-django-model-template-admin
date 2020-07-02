# Для отражения количества экземпляров книги добавьте к модели новый атрибут copy_count. Он должен принимать числовые значения и по умолчанию равняться единице.

# Для отображения стоимости книги добавьте атрибут price. Это числовой атрибут, в котором стоимость выражается в значениях с двумя знаками после запятой.

# class Book(models.Model):  
#     ISBN = models.CharField(max_length=13)  
#     ...
#     copy_count = models.PositiveSmallIntegerField(default=1)
#     price = models.DecimalField(decimal_places=2)

from p_library.models import Author, Book

# Сколько стоит самая дорогая книга?
books = Book.objects.filter()
# >>> [float(b.price) for b in books]
# [939.7, 789.15, 2284.66, 1884.04, 2170.84, 1644.1, 2044.16, 2092.53, 803.6]
max_price_book = books[0]
max_price = float(max_price_book.price)
for b in books:
    if float(b.price) > max_price:
        max_price_book = b
        max_price = float(b.price)
# >>> max_price
# 2284.66

# Сколько в библиотеке копий самой дешёвой книги?
books = Book.objects.filter()
min_price_book = books[0]
min_price = float(min_price_book.price)
for b in books:
    if float(b.price) < min_price:
        min_price_book = b
        min_price = float(b.price)
min_count = min_price_book.copy_count
# >>> min_count
# 1

# Сколько стоят все библиотечные книги авторов, у которых больше одной книги?
authors = Author.objects.filter()
total_cost = 0
for a in authors:
    books = Book.objects.filter(author=a)
    if books.count() > 1:
        for b in books:
            print(b.price, b.copy_count)
            total_cost += float(b.price)*b.copy_count


total_cost = round(total_cost, 2)
# >>> total_cost
# 27169.59

# Сколько стоят все библиотечные книги иностранных писателей?
# >>> [(a.full_name, a.country) for a in Author.objects.filter()]
# [('Николай Васильевич Гоголь', 'RU'), ('Пушкин Александр Сергеевич', 'RU'), ('Тургенев Иван Сергеевич', 'RU'), ('Douglas Adams', 'UK'), ('Jerome David Salinger', 'US'), ('Knut Hamsun', 'NO')]
authors = Author.objects.exclude(country='RU')
total_cost = 0
for a in authors:
    books = Book.objects.filter(author=a)
    for b in books:
        print(b.price, b.copy_count)
        total_cost += float(b.price)*b.copy_count


total_cost = round(total_cost, 2)
# >>> total_cost
# 18792.8

# Сколько стоят все экземпляры Пушкина в библиотеке?
authors = Author.objects.filter(full_name='Пушкин Александр Сергеевич')
total_cost = 0
for a in authors:
    books = Book.objects.filter(author=a)
    for b in books:
        print(b.price, b.copy_count)
        total_cost += float(b.price)*b.copy_count


total_cost = round(total_cost, 2)
total_cost
# 12666.99

# Сколько стоят все книги, автор которых Douglas Adams? Не учитывайте стоимость копий.
authors = Author.objects.filter(full_name='Douglas Adams')
total_cost = 0
for a in authors:
    books = Book.objects.filter(author=a)
    for b in books:
        print(b.price)
        total_cost += float(b.price)


total_cost = round(total_cost, 2)
total_cost