from django.shortcuts import render, redirect
from order.forms import AddOrderForm
import datetime
from order.models import order
from books.models import Header

def Add_Order_Or_User_Add_Order(request):
    if request.user.is_staff:
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
    else:
        if request.method == 'POST':
            form2 = AddOrderForm(request.POST)
            if form2.is_valid():
                order = form2.save(commit=False)
                order.time = form2.cleaned_data['time']
                order.save()
                return redirect('/')
        else:
            form2 = AddOrderForm()

    return render(request, 'html/add_order.html', {
        'form2': form2
    })

def Show_All_Orders(request):
    orders = order.objects.all()
    header = Header.objects.all().first()
    return render(request, 'html/show_all_orders.html', {
        'orders': orders,
        'header': header,
    })