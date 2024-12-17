from typing import List
from datetime import date

from booking import Booking
from room import Room
from customer import Customer
from pricing import PricingStrategy


class Hotel:
    def __init__(self):
        self.rooms: List[Room] = []
        self.bookings: List[Booking] = []

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)
            return f'Room {room.room_number} added to the hotel.'
        return f'Room {room.room_number} already exists in the hotel.'

    def remove_room(self, room_number: str):
        for room in self.rooms:
            if room.room_number == room_number:
                self.rooms.remove(room)
                return f'Room {room_number} removed from the hotel.'
        return f'Room {room_number} does not exist in the hotel.'

    def check_availability(self, room_type, start_date, end_date):
        available_rooms = []
        for room in self.rooms:
            if room.room_type == room_type and room.is_available:
                is_available = True
                for booking in self.bookings:
                    if booking.room == room and booking.is_overlapping(start_date, end_date):
                        is_available = False
                        break
                if is_available:
                    available_rooms.append(room)

        return available_rooms

    def book_room(self, customer: Customer, room: Room, start_date: date, end_date: date, pricing_strategy: PricingStrategy):
        available_rooms = self.check_availability(room.room_type, start_date, end_date)
        if room not in available_rooms:
            return f"Room {room.room_number} is not available for the selected dates."

        booking_id = len(self.bookings) + 1
        total_price = pricing_strategy.calculate_price(start_date, end_date, room)
        booking = Booking(booking_id, customer, room, start_date, end_date, total_price)

        self.bookings.append(booking)
        room.mark_as_booked()

        return f"Booking {booking.booking_id} added to the hotel."

    def list_rooms(self):
        if self.rooms:
            return '\n'.join(f'{room}' for room in self.rooms)

    def list_bookings(self):
        if self.bookings:
            return '\n'.join(f'{booking}' for booking in self.bookings)

    '''    def book_room(self, booking: Booking):
            if booking not in self.bookings:
                self.bookings.append(booking)
                return f'Booking {booking.booking_id} added to the hotel.'
            return f'Booking {booking.booking_id} already exists in the hotel.'''
