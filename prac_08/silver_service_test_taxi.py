"""CP1404 Programming II
Prac 8 Testing SilverServiceTaxi class."""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Fancier Taxi", 100, 2)
    print(taxi)
    taxi.get_fare()
    taxi.drive(18)
    print("Cost of fare = ${:.2f}".format(taxi.get_fare()))


main()
