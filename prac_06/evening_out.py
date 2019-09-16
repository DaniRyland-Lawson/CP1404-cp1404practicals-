"""Program to keep track of appropriate drinking"""

from drink import Drink
from drinklist import DrinkList


def main():
    available_drinks = load_drinks("all_drinks.csv")
    print([str(drink) for drink in available_drinks])


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
