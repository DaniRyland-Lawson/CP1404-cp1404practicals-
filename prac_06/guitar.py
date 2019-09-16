"""CP1404 Programming II, Prac_06 Guitar class"""

CURRENT_YEAR = 2019
VINTAGE_GUITAR_AGE = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{}, ({}), : {:f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_GUITAR_AGE



