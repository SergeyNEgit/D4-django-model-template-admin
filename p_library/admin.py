from django.contrib import admin

# Register your models here.
# from .models import (Book, Author)

# [admin.site.register(item) for item in (Book, Author)]

from p_library.models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count')
