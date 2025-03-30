from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.template.defaultfilters import title
from django.views.generic import ListView, DetailView

from books.models import Book, Genres
from reviews.models import Review


# Create your views here.
class BooksList(ListView):
    model = Book
    paginate_by = 4
    template_name = "main.html"
    context_object_name = 'books_list'

    def get_queryset(self):
        keyword = self.request.GET.get('query')
        books_list = self.model.objects.order_by("title")
        print(f"Initial queryset count: {books_list.count()}")
        if keyword:
            books_list = books_list.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword) |
                                       Q(author__icontains=keyword))
        return books_list

class BooksByGenre(BooksList):
    def get_queryset(self):
        genre_id = self.kwargs.get('genre_id')
        return  self.model.objects.filter(genre_id=genre_id).order_by("title")


class BookInfo(DetailView):
    model = Book
    template_name = "about_book.html"
    context_object_name = 'book_info'
    pk_url_kwarg = 'book_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['review'] = Review.objects.filter(book=self.object.id).order_by("-create_date")
        return context

class BooksByName(BookInfo):
    def get_queryset(self):
        return self.model.objects.filter(book_name=title())