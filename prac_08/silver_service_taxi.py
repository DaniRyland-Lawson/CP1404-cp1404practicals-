"""CP1404 Programming II
Prac 08 - Silver Service Taxi class"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a sting that represents the SilverServiceTaxi"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flag_fall)

    def get_fare(self):
        """Get the current fare with the new flag fall added."""
        return super().get_fare() + self.flag_fall
