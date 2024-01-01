from django.shortcuts import render, redirect
from order.forms import AddOrderForm
import datetime

def Add_Order(request):
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.time = form.cleaned_data['time']
            order.save()
            return redirect('/')
    else:
        form = AddOrderForm()

    return render(request, 'html/add_order.html', {
        'form': form
    })
