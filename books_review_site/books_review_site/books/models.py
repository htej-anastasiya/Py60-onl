from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=160)
    author = models.TextField()
    genre = models.ForeignKey(
        'Genres',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('about_book', kwargs={'book_id': self.pk})

class Genres(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name_plural = "Genres"

    def get_absolute_url(self):
        return reverse('genres', kwargs={'genre_id': self.pk})
