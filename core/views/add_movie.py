from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from core.models import Movie, FavoriteMovie


def add_movie(request):
    if request.method == 'POST':
        movie_db_id = request.POST['movieDB-id']
        movie_title = request.POST['movie-title']
        overview = request.POST['overview']
        date_release = request.POST['date-release']
        uri_image = request.POST['url-image']

        movie = Movie.objects.create(
            the_movie_db_id=movie_db_id,
            movie_title=movie_title,
            overview=overview,
            date=date_release,
            url_image=f"https://image.tmdb.org/t/p/original{uri_image}",
        )

        user = get_object_or_404(User, pk=request.user.id)
        FavoriteMovie.objects.create(user=user, movie=movie)

    return redirect('core:index')
