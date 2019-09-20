"""CP1404 Programming II, Prac_06 Guitar class"""

CURRENT_YEAR = 2019
VINTAGE_GUITAR_AGE = 50


class Guitar:
    """guitar class for storing details of a guitar."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string with details of a Guitar."""
        return "{} ({}) : ${:,.2f} added".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get age of a guitar based on CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage, based on the age of the guitar."""
        return self.get_age() >= VINTAGE_GUITAR_AGE

    def __lt__(self, other):
        """Less than used for sorting the guitars by year release"""
        return self.year < other.year





