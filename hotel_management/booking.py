from datetime import date

class Booking:
    def __init__(self, booking_id: str, customer: 'Customer', room: 'Room', start_date: date, end_date: date, pricing_strategy):
        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.pricing_strategy = pricing_strategy
        self.total_price: float = 0.00

    def calculate_price(self):
        return self.pricing_strategy.calculate_price(self)

    def is_overlapping(self, start_date: date, end_date: date) -> bool:
        return not (self.end_date < start_date or self.start_date > end_date)

    def __str__(self):
        return f'Booking: {self.booking_id}, {self.customer}, {self.room}, Date: {self.start_date}, End: {self.end_date}'


