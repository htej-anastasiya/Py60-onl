from books.models import Genres


def genres_processor(request):
    return {'genres_list': Genres.objects.order_by('genre_name')}