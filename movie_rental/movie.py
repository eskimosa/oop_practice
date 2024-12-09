class Movie:
    def __init__(self, title: str, genre: str, rental_price: float) -> None:
        self.title = title
        self.genre = genre
        self.rental_price = rental_price
        self.is_rented = False

    def rent_movie(self) -> bool:
        if not self.is_rented:
            self.is_rented = True
        else:
            raise Exception(f"Movie '{self.title}' is already rented.")

    def return_movie(self) -> bool:
        if self.is_rented:
            self.is_rented = False
        else:
            raise Exception(f"Movie '{self.title}' is available rented.")

    def __str__(self):
        return f'Movie Title: {self.title}, Genre: {self.genre}, Rental Price: {self.rental_price}, Available to rent: {self.is_rented}'


