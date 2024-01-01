from django import forms
from order.models import order
from books.models import Book
from users.models import User

class AddOrderForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={
        'placeholder': 'کاربر',
        'class': 'form-control'
    }))
    book = forms.ModelChoiceField(queryset=Book.objects.all(), widget=forms.Select(attrs={
        'placeholder': 'کتاب',
        'class': 'form-control'
    }))
    time = forms.DateField(
        input_formats=['%Y-%m-%d'], 
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }, format='%Y-%m-%d')
    )
    class Meta:
        model = order
        fields = ('user', 'book', 'time')

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
        return order
