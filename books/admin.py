from django.contrib import admin
from books.models import Book
from books.models import UserDetails

admin.site.register(Book)
admin.site.register(UserDetails)

