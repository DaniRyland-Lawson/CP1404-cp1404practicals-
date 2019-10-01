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
            current_taxi = taxis[taxi_choice]
            print("Bill to date: ${:.2f}".format(taxis[taxi_choice].get_fare()))
        elif user_choice == "D":
            pass

    else:
        print("Invalid Menu selection")

def list_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))
main()
