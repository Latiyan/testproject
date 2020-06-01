from django.shortcuts import render, redirect
from datetime import datetime
from .models import Products


# Create your views here.
def index(request):
    return render(request, 'home.html')


def listing(request):
    if request.method == 'POST':
        context = {
            'products': Products.objects.filter(name=request.POST.get('name'))
        }
    else:
        context = {
            'products': Products.objects.all()
        }

    return render(request, 'listing.html', context)


def add(request):
    return render(request, 'add.html')


def edit(request, id):
    context = {
        'product': Products.objects.get(id=id)
    }

    return render(request, 'edit.html', context)


def addnew(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        date_created = datetime.today()
        product = Products(name=name, description=description, price=price, date_created=date_created)

        product.save()

    return redirect('/listing')


def update(request, id):
    product = Products.objects.get(id=id)
    product.name = request.POST.get('name')
    product.description = request.POST.get('description')
    product.price = request.POST.get('price')

    product.save()

    return redirect('/listing')


def delete(request, id):
    product = Products.objects.get(id=id)
    product.delete()

    return redirect('/listing')
