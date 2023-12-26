from django.db import models

class BookShelf(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    bookshelf = models.ForeignKey(BookShelf, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_images', blank=True, null=True)
    name = models.CharField(max_length = 255)
    code = models.CharField(max_length = 20)
    author = models.CharField(max_length = 255)
    price = models.CharField(max_length = 15)
    publisher = models.CharField(max_length = 255)
    is_available = models.BooleanField(default = True)
    createdAt = models.TimeField(auto_now_add = True)
    updatedAt = models.TimeField(auto_now = True)

    def __str__(self):
        return f"{self.name } > {self.author}"