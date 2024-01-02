from django.db import models
from users.models import User
from books.models import Book

class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    time = models.DateField()

class order_from_request_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    time = models.DateField()
    status = models.BooleanField(default=False)
    