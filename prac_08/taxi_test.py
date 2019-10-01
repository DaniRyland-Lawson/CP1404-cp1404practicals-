"""CP1404 Programming II
Test Taxi Prac."""


from prac_08.taxi import Taxi


def main():
    new_taxi = Taxi("Prius 1", 100, price_per_km=1.23)
    new_taxi.drive(40)
    print(new_taxi)

    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)


main()
