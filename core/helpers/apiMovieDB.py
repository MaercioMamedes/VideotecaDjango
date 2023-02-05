import requests
from dotenv import load_dotenv
import os


class ClientTheMovieDB:
    def __init__(self):
        load_dotenv()
        self.api_key = str(os.getenv('API_KEY'))

    def search_movie(self, title_movie):
        url_base = f'https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&query={title_movie}&language=pt-BR'
        data_movies = requests.get(url_base).json()
        return dict(data_movies)
