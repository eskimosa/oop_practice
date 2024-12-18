from datetime import date
from hotel import Hotel
from room import Room
from customer import Customer


def main():
    hotel = Hotel()

    room1 = Room('101', 'Single', 100)
    room2 = Room('102', 'Single', 100)
    room3 = Room('201', 'Double', 200)
    room4 = Room('202', 'Double', 200)

    print(hotel.add_room(room1))
    print(hotel.add_room(room2))
    print(hotel.add_room(room3))
    print(hotel.add_room(room4))
    print(hotel.add_room(room1))  # Should return room 101 already exists

    print("\n--- List of Rooms ---")
    print(hotel.list_rooms())

    print("\nRemoving room 102...")
    print(hotel.remove_room('102'))  # Should remove room 102
    print(hotel.remove_room('999'))  # Should return room does not exist

    print("\n--- List of Rooms after removal ---")
    print(hotel.list_rooms())

    customer1 = Customer('C001', 'Alice', False)
    customer2 = Customer('C002', 'Bob', True)

    start_date = date(2024, 12, 18)
    end_date = date(2024, 12, 20)

    print("\n--- Booking a Room ---")
    print(hotel.book_room(customer1, room1, start_date, end_date))  # Should book room 101 for Alice

    print("\n--- List of Bookings ---")
    print(hotel.list_bookings())

    print("\nTrying to book the same room for the same period (room should not be available):")
    print(hotel.book_room(customer2, room1, start_date, end_date))

    weekend_start = date(2024, 12, 21)  # This period includes a weekend (Saturday/Sunday)
    weekend_end = date(2024, 12, 23)
    print("\n--- Booking a Room for Weekend Pricing ---")
    print(hotel.book_room(customer1, room3, weekend_start, weekend_end))  # Should apply weekend pricing

    loyal_start = date(2024, 12, 24)
    loyal_end = date(2024, 12, 25)
    print("\n--- Booking a Room for Loyal Member ---")
    print(hotel.book_room(customer2, room4, loyal_start, loyal_end))  # Should apply loyalty member pricing

    print("\n--- Final List of Bookings ---")
    print(hotel.list_bookings())

    one_day_start = date(2024, 12, 26)
    one_day_end = date(2024, 12, 26)
    print("\n--- Booking for Just One Day ---")
    print(hotel.book_room(customer1, room1, one_day_start, one_day_end))  # Should fail since room1 is already booked


if __name__ == "__main__":
    main()

