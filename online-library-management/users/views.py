from django.shortcuts import render, redirect
from users.forms import SignupForm
from users.models import UserProfile

def Add_User(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("user aded sucsse")
            return redirect('/')
    else:
        form = SignupForm

    return render(request, 'html/add_user.html', {
        'form': form
    })

def Show_Users(request):
    users = UserProfile.objects.all()
    return render(request, 'html/show_users.html', {
        'users': users
    })