from django.contrib import admin
from books.models import Book, BookShelf, Header

admin.site.register(Book)
admin.site.register(BookShelf)
admin.site.register(Header)