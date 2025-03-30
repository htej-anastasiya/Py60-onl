from django.contrib import admin
from django.urls import path, include

from books.views import *

urlpatterns = [
    path('', BooksList.as_view(),name='index'),
    path('search', BooksList.as_view(), name='search'),
    path('genres/<int:genre_id>', BooksByGenre.as_view(), name='genres'),
    path('book-info/<int:book_id>', BookInfo.as_view(), name='about_book'),
    path('book-info/<int:book_id>/reviews/', include(("reviews.urls", "reviews"), namespace='book_reviews')),
]
