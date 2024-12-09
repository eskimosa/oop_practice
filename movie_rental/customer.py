from typing import List
from movie import Movie


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rented_movies = {}
        self.total_spent = 0.00

    def rent_movie(self, movie, rental_duration):
        if movie.title in self.rented_movies:
            return f"{self.name} already rented the movie '{movie.title}'."

        if not movie.is_rented:
            movie.rent_movie()
            self.rented_movies[movie.title] = (movie, rental_duration)
            self.total_spent += movie.rental_price * rental_duration
        else:
            return f"Movie '{movie.title}' is not available for rent."

    def return_movie(self, movie: Movie):
        if movie.title in self.rented_movies:
            movie.return_movie()
            del self.rented_movies[movie.title]
        else:
            return f"{self.name} did not rent the movie '{movie.title}'."

    def __str__(self):
        rented_count = len(self.rented_movies)
        return f"Name: {self.name}, Movies Rented: {rented_count}, Total Spent: ${self.total_spent:.2f}"

