"""CP1404 Programming II Prac_06
Test guitar ages from input"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2019


def main():
    """Tests for the Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.90)

    print("{} get_age() - expected {}. Got {}".format(guitar.name, 95, guitar.get_age()))
    print("{} get_age() - expected {}. Got {}".format(other.name, 95, other.get_age()))

    print("{} is_vintage() - expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - expected {}. Got {}".format(other.name, False, other.is_vintage()))


main()
