from django.contrib import admin

# Register your models here.
from books.models import Book, Genres


@admin.register(Book)
class BookItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')

@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('genre_name',)
