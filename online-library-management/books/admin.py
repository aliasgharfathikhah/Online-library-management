from django.contrib import admin
from books.models import Book, BookShelf

admin.site.register(Book)
admin.site.register(BookShelf)