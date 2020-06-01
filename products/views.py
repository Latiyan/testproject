from django.shortcuts import render, redirect
from datetime import datetime
from .models import Products


# Create your views here.
def index(request):
    context = {
        #
    }

    return render(request, 'home.html', context)


def listing(request):
    context = {
        #
    }

    return render(request, 'listing.html', context)


def add(request):
    context = {
        #
    }

    return render(request, 'add.html', context)


def addnew(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        date_created = datetime.today()
        product = Products(name=name, description=description, price=price, date_created=date_created)

        product.save()

    return redirect('/listing')
