from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext

from books.models import Book, Genres


# Create your views here.

def index(request):
    books_list = Book.objects.order_by("title")
    context = {'books_list': books_list}
    return render(request, "main.html", context)

def books_by_genre(request, genre_id):
    books_list = Book.objects.filter(genre_id=genre_id).order_by("title")
    context = {'books_list': books_list}
    return render(request, "main.html", context)

def get_info_about_book(request, book_id):
    try:
        book_info = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book hot found")
    context = {'book_info': book_info}
    return render(request,'about_book.html', context)