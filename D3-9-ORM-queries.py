from p_library.models import Author, Book

pushkin = Author.objects.get(full_name="Пушкин Александр Сергеевич")

pushkin_books = Book.objects.filter(author=pushkin)

pushkin_books.exists()
pushkin_books.count()

for book in pushkin_books:
    print(book.title)

no_horsman_books = pushkin_books.exclude(title__contains="всадник")

for book in no_horsman_books:
    print(book.title)

# двойное подчёркивание ()== WHERE) в аргументе exclude: title__contains="всадник". 
# регистронезависимая строка - вместо contains - icontains


no_horsman_pushkin_books = Book.objects.all().filter(author=pushkin).exclude(title__icontains="всадник")

for book in no_horsman_pushkin_books:
    print(book.title)