from django.contrib import admin
from django.urls import path, include

from books.views import *

urlpatterns = [
    path('', index, name='index'),
    path('genres/<int:genre_id>', books_by_genre, name='genres'),
    path('book-info/<int:book_id>', get_info_about_book, name='about_book'),
]
