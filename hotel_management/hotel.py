from typing import List
from datetime import date, timedelta

from booking import Booking
from room import Room
from customer import Customer
from pricing import PricingStrategy, WeekendPricing, StandardPricing, LoyaltyMemberPricing


class Hotel:
    def __init__(self):
        self.rooms: List[Room] = []
        self.bookings: List[Booking] = []
        self.pricing_strategy = PricingStrategy

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

    def check_availability(self, room_type: str, start_date: date, end_date: date) -> List[Room]:
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

    def get_weekdays_and_weekends(self, start_date, end_date):
        weekdays = 0
        weekends = 0

        current_date = start_date
        while current_date < end_date:
            if current_date.weekday() < 5:
                weekdays += 1
            else:
                weekends += 1
            current_date += timedelta(days=1)

        return weekdays, weekends

    def book_room(self, customer: Customer, room: Room, start_date: date, end_date: date):
        available_rooms = self.check_availability(room.room_type, start_date, end_date)
        if room not in available_rooms:
            return f"Room {room.room_number} is not available for the selected dates."

        booking_id = str(len(self.bookings) + 1)
        weekdays, weekends = self.get_weekdays_and_weekends(start_date, end_date)
        if customer.is_loyal_member:
            pricing_strategy = LoyaltyMemberPricing()
        elif weekends > 0:
            pricing_strategy = WeekendPricing()
        else:
            pricing_strategy = StandardPricing()

        total_price = pricing_strategy.calculate_price(weekdays, weekends, room)
        booking = Booking(booking_id, customer, room, start_date, end_date, total_price)

        self.bookings.append(booking)
        room.mark_as_booked()

        return f"Booking {booking.booking_id} added to the hotel, total price: {total_price}."

    def list_rooms(self):
        if self.rooms:
            return '\n'.join(f'{room}' for room in self.rooms)

    def list_bookings(self):
        if self.bookings:
            return '\n'.join(f'{booking}' for booking in self.bookings)

