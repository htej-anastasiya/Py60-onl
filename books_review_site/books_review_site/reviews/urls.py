from django.urls import path, include

from comments.views import CommentAdd
from reviews.views import *

urlpatterns = [
    path('',ReviewList.as_view(), name='reviews_list'),
    path('search', ReviewList.as_view(), name='search'),
    path('add/',ReviewAdd.as_view(), name='add_review'),
    path('update/<int:pk>',ReviewUpdate.as_view(), name='update_review'),
    path('delete/<int:pk>',ReviewDelete.as_view(), name='delete_review'),
    path('<int:pk>',ReviewInfo.as_view(), name='show_more_review'),
]