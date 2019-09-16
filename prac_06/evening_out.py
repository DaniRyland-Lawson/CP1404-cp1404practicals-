"""Program to keep track of appropriate drinking"""

from prac_06.drink import Drink
from prac_06.drinklist import DrinkList


def main():
    available_drinks = load_drinks("all_drinks.csv")

def load_drinks(filename):
    all_drinks = []
    input_file = open(filename)
    for line in input_file:
        parts = line.strip().split(",")
        print(parts)
    input_file.close()
    return all_drinks


main()
