from datetime import date
from customer import Customer
from room import Room


class Booking:
    def __init__(self, booking_id: str, customer: 'Customer', room: 'Room', start_date: date, end_date: date, total_price: float):
        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = total_price

    def is_overlapping(self, start_date: date, end_date: date) -> bool:
        return not (self.end_date < start_date or self.start_date > end_date)

    def __str__(self):
        return f'Booking: {self.booking_id}, {self.customer}, {self.room}, Date: {self.start_date}, End: {self.end_date}, Total booking price: {self.total_price}'


