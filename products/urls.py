from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='HomePage'),
    path('home', views.index, name='HomePage'),
    path('listing', views.listing, name='ProductListing'),
    path('add', views.add, name='AddNewProduct'),
]
