# Create a class for representing a movie with some attributes (title, director, duration, actors, rating) and behavior
# (find if movie director name starts with specific symbol, find if some person is an actor, change rating),
# create several movies and perform operations on them, check how many movies are created.

class Movie:
    def __init__(self, title: str, director: str, actors: list, rating: int):
        self.title = title
        self.director = director
        self.actors = actors
        self.rating = rating

    def director_name(self, name_symbol: str):
        if name_symbol in self.director:
            print(f"{name_symbol} exists in director's name")

    def movie_cast(self, movie_star: str):
        if movie_star in self.actors:
            print(f"{movie_star} is casting in this movie")

    def new_rating(self, rating_number: int):
        self.rating = rating_number
        print(f'{self.rating} is the new rating of this movie')


movie = Movie('Friends', 'Tom Hanks', ['Tom Cruse', 'Tom Hardy', 'James May', 'Richard Hammond'], 8)
movie.director_name('o')
movie.movie_cast('Tom Hardy')
movie.new_rating(10)
