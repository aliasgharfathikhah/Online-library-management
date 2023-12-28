from django import forms
from books.models import Book

class AddBookForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.TextInput(attrs={
        'placeholder': 'عکس کتاب',
        'class': 'form-control'
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام کتاب',
        'class': 'form-control'
    }))
    code = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'کد کتاب',
        'class': 'form-control'
    }))
    author = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نویسنده',
        'class': 'form-control'
    }))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'قیمت',
        'class': 'form-control'
    }))
    publisher = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'ناشر',
        'class': 'form-control'
    }))

    class Meta:
        model = Book
        fields = ('image', 'name', 'code', 'author', 'price', 'publisher')

    def save(self, commit=True):
        book = super().save(commit=False)
        if commit:
            book.save()
        return book
