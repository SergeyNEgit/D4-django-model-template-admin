# django-model-template-admin на основе django проекта \D3-Django\my_site\ с приложением p_library

D4.11
Книги издают разные издательские дома. Издательства следят за качеством переводов и издаваемой продукции. Добавим в нашу библиотеку новую модель и отсортируем книги по издательству.

Вам нужно сделать вот что:

• Добавить новую модель — Издательства. Для каждого издательства необходимо создать связь с Книгой.

• Создать несколько Издательств, связать их с Книгами и вывести в отдельном Django-шаблоне в виде списка <ul><li><>/li</ul> с подключенным bootstrap. Шаблон должен открываться в отличном от созданных нами URL'е.

Добавление издательства и связи Книга-Издательство нужно сделать в отдельной панели в админке.

Источник <https://lms.skillfactory.ru/

Для просмотра решения нужно: 
1) использовать окружение с установленным
	Django==3.0.7 
2) скопировать проект:
	...>git clone https://github.com/SergeyNEgit/django-model-template-admin.git
3) запустить сервер:
	...>python manage.py runserver
4) открыть:
	http://127.0.0.1:8000/publishers/


Далее - конспект решения.

0. создаем git репозиторий на основе django-project: ...\D3-Django\my_site
Источник <https://github.com/SergeyNEgit/django-model-template-admin> 

...>cd C:\ESNdocs\edX-Py\D3-Django\my_site
...>echo "# django-model-template-admin на основе \D3-Django\my_site" >> README.md
...>git init
...>git add .
...>git commit -m "1st commit: add . from \D3-Django\my_site"
...>git remote add origin https://github.com/SergeyNEgit/django-model-template-admin.git
...>git push -u origin master


...>cd ...\D4-django-template-admin
...>git clone https://github.com/SergeyNEgit/django-model-template-admin.git

переносим виртуальное окружение D3\django.venv в edx-py\
1. активируем D3\django.venv и сохраняем его конфигурацию, деактивируем 
edx-py> D3-Django\django.venv\Scripts\activate.bat
edx-py> pip freeze >requirements.txt
edx-py> D3-Django\django.venv\Scripts\deactivate.bat

2. создаем D.venv и формируем эквивалент окружения D3\django.venv 
edx-py> python -m venv edx-py\D.venvdamp
edx-py> pip install -r requirements.txt

3. запускам сервер django в D4
edx-py\D4-django-template-admin-library> python manage.py runserver

4. описываем модель Publisher в файле 
p_library\models.py:
  …
class Publisher(models.Model):  
    name = models.TextField()  
    description = models.TextField()  
    def __str__(self):
    
  создаем описание миграции и проводим миграцию:
…> python manage.py makemigrations
	Migrations for 'p_library':
	  p_library\migrations\0002_publisher.py
	    - Create model Publisher
…> python manage.py migrate
	Operations to perform:
	  Apply all migrations: admin, auth, contenttypes, p_library, sessions
	Running migrations:
	  Applying p_library.0002_publisher... OK
	
…>python manage.py shell
	…
	>>> from p_library.models import Publisher as p
	>>> p.objects.all()
	<QuerySet []>
	
5. Добавляем панель Publisher в admin-ку
p_library/admin.py
…
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
  pass

6. Создаем запись в Publisher через admin-ку
	>>> 1|Детгиз|Книги для детей и их родителей

7. Добавляем внешний ключ в описание Book, related_name='books' - чтобы можно было вызвать список книг: pablisher.books - 
в p_library/models.py. В качестве значения по умолчанию указываем "1" (Детгиз)

	>>>python manage.py migrate
		Operations to perform:
		  Apply all migrations: admin, auth, contenttypes, p_library, sessions
		Running migrations:
		  Applying p_library.0003_book_publisher... OK
редактируем список издательств и книг, указываем ссылки.

8. Создаем шаблон publishers.html
используем явное определение html страницы, подключаем bootstrap4:
 <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
выводим издательства и книги, ими выпущенные:
    <p class="h3">Все издательства моей библиотеки <span class="badge badge-primary badge-pill">{{publishers|length}}</span></p>
    <ul class="list-group">
        {% for p in publishers %}
            <li class="list-group-item h5">{{p.0.name}} - {{p.0.description}} 
                <span class="badge badge-primary badge-pill">{{p.1|length}}</span></li>
            <ul class="list-group-secondary">
                {% for b in p.1 %}
                    <li class="list-group-item h7">{{b.title}}, {{b.author}}</li>
                {% endfor %}
            </ul>
        {% endfor %}
    </ul>

9. Обновляем репозиторий
	(D.venv) …>git add .
	(D.venv) …>git commit -m "D4.11 add . from \D3C:\ESNdocs\edX-Py\D4-django-model-template-admin"
  	(D.venv) …>git push -u origin master
  
