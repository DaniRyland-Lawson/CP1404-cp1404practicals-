"""CP1404 Programming II
Prac 08 Taxi Simulator"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    user_choice = input(">>>").upper()

    while user_choice != "Q":
        if user_choice == "C":
            print("Taxi's available:")
            list_taxis(taxis)
            taxi_choice = int(input("Choose Taxi: "))
            print("Bill to date: ${:.2f}".format(taxis[taxi_choice].get_fare()))
        elif user_choice == "D":
            current_taxi = Taxi(None, 0)
            current_taxi.start_fare()
            distance_driven = float(input("Drive how far? "))
            current_taxi.drive(distance_driven)
            trip_cost = current_taxi.get_fare()
            total_cost += trip_cost
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
        else:
            print("Invalid Menu selection")
        print(MENU)
        user_choice = input(">>>").upper()

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxi's are now:")
    list_taxis(taxis)


def list_taxis(taxis, ):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
