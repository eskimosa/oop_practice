from abc import ABC, abstractmethod
from room import Room
from datetime import timedelta


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, weekdays, weekends, room: 'Room'):
        pass


class StandardPricing(PricingStrategy):
    def calculate_price(self, weekdays, weekends, room):
        total_price = room.base_price * (weekdays + weekends)
        return total_price


class WeekendPricing(PricingStrategy):
    def calculate_price(self, weekdays, weekends, room):
        weekends_price = (room.base_price * 1.2) * weekends
        total_price = room.base_price * weekdays + weekends_price
        return total_price


class LoyaltyMemberPricing(PricingStrategy):
    def calculate_price(self, weekdays, weekends, room):
        weekday_price = room.base_price * weekdays
        weekend_price = (room.base_price * 1.2) * weekends
        total_price = weekday_price + weekend_price

        loyalty_discount = 0.15
        total_price_with_discount = total_price * (1 - loyalty_discount)
        return total_price_with_discount
