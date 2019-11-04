"""Program to keep track of appropriate drinking"""

from drink import Drink
from drinklist import DrinkList

MENU = ("Menu:")


def main():
    available_drinks = load_drinks("all_drinks.csv")
    # print([str(drink) for drink in available_drinks])
    my_drinks = DrinkList()
    print(MENU)
    menu_choice = input(">").lower()
    while menu_choice != "q":
        if menu_choice == "a":
            display_available_drinks(available_drinks)
            drink_choice = int(input("?"))
            my_drinks.add(available_drinks[drink_choice])
        else:
            print("Invalid choice")
        print(my_drinks)
        print(MENU)
        menu_choice = input(">").lower()
    print(
        "You drank {} drinks, ({} were alcoholic for a total of {}ml alcohol), which cost ${:.2f}".format(
            len(my_drinks), my_drinks.get_number_alcoholic(), my_drinks.get_alcohol_content(),
            my_drinks.get_total_price()))


def display_available_drinks(drinks):
    print([(i, str(drink)) for i, drink in enumerate(drinks)])


def load_drinks(filename):
    """Loading drink list from csv file"""
    all_drinks = []
    input_file = open(filename)
    for line in input_file:
        """Stripping the line of the /n and splitting it at "," commas."""
        parts = line.strip().split(",")
        # print(parts)
        all_drinks.append(Drink(parts[0], float(parts[1]), float(parts[2]), float(parts[3])))
    input_file.close()
    return all_drinks


main()
