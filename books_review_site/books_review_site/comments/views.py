from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from comments.forms import CommentForm
from comments.models import Comment
from reviews.models import Review


# Create your views here.
class CommentAdd(LoginRequiredMixin, CreateView):
    login_url = "login"
    redirect_field_name = "redirect_to"
    model = Comment
    template_name = "review_info.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("review_info", kwargs={"review_id": self.kwargs["review_id"]})

    def form_valid(self, form):
        # print("Form data:", form.cleaned_data)
        # print("Book ID from URL:", self.kwargs.get("book_id"))
        # print("Current user:", self.request.user.id)
        form.instance.user = self.request.user
        form.instance.book = Review.objects.get(pk=self.kwargs["review_pk"])
        return super().form_valid(form)