import requests


class ClientTheMovieDB:
    def __init__(self):
        self.api_key = '328a263ac28892407a8153e3133e8a5c'

    def search_movie(self, title_movie):
        url_base = f'https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&query={title_movie}&language=pt-BR'
        data_movies = requests.get(url_base).json()
        return dict(data_movies)
