from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='home'),
    path('add/', views.add_book, name='addbook'),
    path('show/', views.show_book, name='showbook'),
    path('edit/', views.edit_book, name='editbook'),
    path('search/', views.search_book, name='searchbook'),
    path('contact/', views.contact_us, name='contactus'),
]