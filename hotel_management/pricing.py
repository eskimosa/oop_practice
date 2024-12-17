from abc import ABC, abstractmethod


class PricingStrategy(ABC):

    @abstractmethod
    def calculate_price(self, booking):
        pass
    # Abstract method to calculate the price for a booking.

class StandardPricing(PricingStrategy):

    def calculate_price(self, booking):
        pass
        # charge the base price of the room per day.


class WeekendPricing(PricingStrategy):
    def calculate_price(self, booking):
        pass
    #  to apply a higher rate on weekends; The price should increase by 20% on weekends (Saturday and Sunday).


class LoyaltyMemberPricing(PricingStrategy):

    def calculate_price(self, booking):
        pass
    #  apply a discount for loyal customers; Loyal customers (with is_loyal_member set to True) receive a 15% discount on all bookings.


