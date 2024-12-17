from room import Room
from booking import Booking
from customer import Customer
from hotel import Hotel
from datetime import date
from pricing import PricingStrategy, StandardPricing, WeekendPricing, LoyaltyMemberPricing


def start():
    hotel = Hotel()

    room_1 = Room('1', 'double', 127.90)
    room_2 = Room('2', 'single', 100.00)
    room_3 = Room('3', 'double', 150.00)

    print('Adding rooms...')
    print(hotel.add_room(room_1))
    print(hotel.add_room(room_2))
    print(hotel.add_room(room_3))

    print('Listing rooms from hotel...')
    print(hotel.list_rooms())

    print('Removing rooms...')
    print(hotel.remove_room('3'))

    print('Listing rooms after removal of 3 from hotel...')
    print(hotel.list_rooms())

    print('Marking room as booked:')
    print(room_1.mark_as_booked())
    print('Listing rooms after marking one as booked...')
    print(hotel.list_rooms())

    print('Marking room as available:')
    print(room_1.mark_as_available())
    print('Listing rooms after marking one as available...')
    print(hotel.list_rooms())

    print('Marking room as available:')
    print(room_1.mark_as_available())
    print('Listing rooms after marking one as available...')
    print(hotel.list_rooms())

    print('Adding Customers...')
    albert = Customer('1', 'Albert', True)
    genia = Customer('2', 'Genia', True)

    print(albert)
    print(genia)

    pricing_strategy = StandardPricing()

    print('Adding Bookings...')
    hotel.book_room(albert, room_1, date(2024, 12, 15), date(2024, 12, 20), pricing_strategy)

    # Check availability for a "single" room from 2024-12-03 to 2024-12-04
    available_rooms = hotel.check_availability("single", date(2024, 12, 3), date(2024, 12, 4))
    print([room.room_number for room in available_rooms])


if __name__ == '__main__':
    start()
