from django.contrib import admin

# Register your models here.
# from .models import (Book, Author)

# [admin.site.register(item) for item in (Book, Author)]

from p_library.models import Author, Book, Publisher

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    # отображаемые в списке поля, включая "вычисляемое" author_full_name.
    list_display = ('title', 'author_full_name', 'publisher')

    # редактируемые поля. По умолчанию - все.
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count', 'publisher')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
