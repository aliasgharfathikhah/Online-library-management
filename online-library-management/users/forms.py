from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.models import UserProfile


class SignupForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام',
        'class': 'form-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام خانوادگی',
        'class': 'form-control'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'شماره تلفن',
        'class': 'form-control'
    }))
    nationalid = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'کد ملی',
        'class': 'form-control'
    }))
    City = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'شهر',
        'class': 'form-control'
    }))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'سن',
        'class': 'form-control'
    }))
    GENDER_CHOICES = [
        ('male', 'مرد') ,
        ('female', 'زن'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'name', 'last_name', 'phone', 'nationalid', 'City', 'age', 'gender')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'نام کاربری',
        'class': 'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'ایمیل',
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'رمز عبور',
        'class': 'form-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'تکرار رمز عبور',
        'class': 'form-control'
    }))


    def save(self, commit=True):
        user = super().save(commit=False)
        name = self.cleaned_data.get('name')
        last_name = self.cleaned_data.get('last_name')
        phone = self.cleaned_data.get('phone')
        nationalid = self.cleaned_data.get('nationalid')
        City = self.cleaned_data.get('City')
        age = self.cleaned_data.get('age')
        gender = self.cleaned_data.get('gender')
        if commit:
            user.save()
            UserProfile.objects.create(user=user, name=name, last_name=last_name, phone=phone, nationalid=nationalid, City=City, age=age, gender=gender)
        return user
