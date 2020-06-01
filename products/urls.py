from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('listing', views.listing, name='listing'),
    path('add', views.add, name='add'),
    path('addnew', views.addnew, name='addnew'),
]
