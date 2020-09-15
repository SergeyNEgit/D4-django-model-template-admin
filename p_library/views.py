from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from p_library.models import Book, Publisher


# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку", 
        "books": books,
        "range100" : [i for i in range(1, 100) if i%3 == 0],
    }
    return HttpResponse(template.render(biblio_data, request))
# Мы добавили request в рендеринг. Теперь при открытии нашего сайта в форму добавится CSRF.

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def publishers_list(request):
    template = loader.get_template('publishers.html')
    books = Book.objects.all()
    publishers = Publisher.objects.all()
    biblio_data = {
        "publishers": [(p, books.filter(publisher=p.id)) for p in publishers]
    }
    return HttpResponse(template.render(biblio_data, request))