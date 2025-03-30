from django.http import HttpResponseForbidden


class ReviewOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user.id != object.review_author.id:
            return HttpResponseForbidden("You're not allowed to perform this action")
        return super().dispatch(request, *args, **kwargs)