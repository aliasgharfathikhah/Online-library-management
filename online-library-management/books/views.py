from django.shortcuts import render
from books.models import Book, BookShelf, Header

def home(request):
    books = Book.objects.all()
    header = Header.objects.all().first()

    return render(request, 'html/home.html', {
        'books': books,
        'header': header,
    })
