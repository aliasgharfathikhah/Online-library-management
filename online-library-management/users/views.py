from django.shortcuts import render, redirect
from users.forms import SignupForm

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