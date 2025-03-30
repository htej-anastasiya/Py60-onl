from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from books.models import Book
from comments.forms import CommentForm
from comments.models import Comment
from config.views import ReviewOwnerRequiredMixin
from reviews.forms import ReviewForm
from reviews.models import Review


# Create your views here.

class ReviewList(ListView):
    paginate_by = 4
    model = Review
    template_name = "review_list.html"
    context_object_name = 'review_list'

    def get_queryset(self):
        keyword = self.request.GET.get('query')
        review_list = self.model.objects.order_by("-create_date")
        print(f"Initial queryset count: {review_list.count()}")
        if keyword:
            review_list = review_list.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword) |
                                             Q(review_author__username__icontains=keyword) | Q(
                book__title__icontains=keyword))
        return review_list


class ReviewAdd(LoginRequiredMixin, CreateView):
    login_url = "login"
    redirect_field_name = "redirect_to"
    model = Review
    template_name = "add_review.html"
    form_class = ReviewForm

    def get_success_url(self):
        return reverse("about_book", kwargs={"book_id": self.kwargs["book_id"]})

    def form_valid(self, form):
        # print("Form data:", form.cleaned_data)
        # print("Book ID from URL:", self.kwargs.get("book_id"))
        # print("Current user:", self.request.user.id)
        form.instance.review_author = self.request.user
        form.instance.book = Book.objects.get(pk=self.kwargs["book_id"])
        return super().form_valid(form)


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"
    redirect_field_name = "redirect_to"
    model = Review
    template_name = "update_review.html"
    form_class = ReviewForm

    def get_success_url(self):
        return reverse("about_book", kwargs={"book_id": self.kwargs["book_id"]})

class ReviewDelete(LoginRequiredMixin, ReviewOwnerRequiredMixin,DeleteView):
    login_url = "login"
    redirect_field_name = "redirect_to"
    model = Review
    template_name = "delete_review.html"

    def get_success_url(self):
        return reverse("about_book", kwargs={"book_id": self.kwargs["book_id"]})

# class ReviewInfo(DetailView):
#     model = Review
#     template_name = "review_info.html"
#     context_object_name = 'review_view'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         context['comment'] = Comment.objects.filter(review=self.object.id).order_by("-created_at")
#         return context


class ReviewInfo(FormMixin, DetailView):
    model = Review
    template_name = "review_info.html"
    context_object_name = 'review_view'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('show_more_review', kwargs={'pk': self.object.pk})

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['comment'] = Comment.objects.filter(review=self.object.id).order_by("-created_at")
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.review = self.object
        comment.user = self.request.user
        comment.save()
        return redirect(self.request.path)