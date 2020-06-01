from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('listing', views.listing),
    path('add', views.add),
    path('edit/<int:id>', views.edit),
    path('addnew', views.addnew),
    path('update/<int:id>', views.update),
]
