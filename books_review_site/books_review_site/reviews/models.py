from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse

from books.models import Book
from config import settings
from user.models import CustomUser

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]

# Create your models here.
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, blank=False, related_name='reviews')
    review_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), null=False, blank=False,
                                      related_name='reviews')
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review of {self.book.title} by {self.review_author.username}"

    def get_absolute_url(self):
        return reverse('reviews:show_more_review', kwargs={'pk': self.pk})