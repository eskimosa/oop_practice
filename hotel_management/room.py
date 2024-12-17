class Room:
    def __init__(self, room_number: str, room_type: str, base_price: float):
        self.room_number = room_number
        self.room_type = room_type
        self.base_price = base_price
        self.is_available: bool = True

    def mark_as_booked(self):
        if self.is_available:
            self.is_available = False
            return f'Room {self.room_number} is booked.'
        return f'Room {self.room_number} is available.'

    def mark_as_available(self):
        if not self.is_available:
            self.is_available = True
            return f'Room {self.room_number} is available.'
        return f'Room {self.room_number} is not available.'

    def __str__(self):
        return f'Room number: {self.room_number}, Room type: {self.room_type}, base price: {self.base_price}, Status: {"Available" if self.is_available else "Booked"}'
