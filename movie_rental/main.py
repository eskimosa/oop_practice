from rental_system import RentalSystem
from movie import Movie
from customer import Customer


def main():
    rental_system = RentalSystem()

    # Adding Movies
    rental_system.add_movie(Movie("The Matrix", "Sci-Fi", 5.0))
    rental_system.add_movie(Movie("Inception", "Action", 7.5))

    # Adding Customers
    customer_john = Customer("John Doe")
    rental_system.add_customer(customer_john)
    print(rental_system.list_customers())
    print(rental_system.list_movies())

    # Rent a movie
    movie_inception = rental_system.get_movie_by_title("Inception")
    if movie_inception:
        customer_john.rent_movie(movie_inception, rental_duration=3)

    movie_the_matrix = rental_system.get_movie_by_title("The Matrix")
    if movie_the_matrix:
        customer_john.rent_movie(movie_the_matrix,rental_duration=5)

    # Return a movie
    customer_john.return_movie(movie_inception)

    # List movies and customers
    print("Movies in Rental System:")
    print(rental_system.list_movies())

    print("\nCustomers in Rental System:")
    print(rental_system.list_customers())


if __name__ == "__main__":
    main()