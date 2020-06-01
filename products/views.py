from django.shortcuts import render


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
