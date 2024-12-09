from movie import Movie


class RentalSystem:
    def __init__(self):
        self.movies = {}
        self.customers = {}

    def add_movie(self, movie: Movie):
        if movie.title in self.movies:
            return f"Movie '{movie.title}' already exists in the system."
        self.movies[movie.title] = movie

    def list_movies(self) -> str:
        if len(self.movies) == 0:
            return 'No movies found'
        return "\n".join(str(movie) for movie in self.movies.values())

    def add_customer(self, customer):
        if customer.name in self.customers:
            raise Exception(f"Customer '{customer.name}' already exists in the system.")
        self.customers[customer.name] = customer

    def list_customers(self) -> str:
        return "\n".join(str(customer) for customer in self.customers.values())

    def get_movie_by_title(self, title):
        return self.movies.get(title, None)

    def get_customer_by_name(self, name):
        return self.customers.get(name, None)


