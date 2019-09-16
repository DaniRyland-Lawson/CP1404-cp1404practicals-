"""Drink class."""


# name, price, alcohol_content (%), volume

class Drink:
    MINIMUM_ALCOHOL_THRESHOLD = 0.01

    def __init__(self, name="", price=0.0, volume=0.0, alcohol_content=0.0):
        self.name = name
        self.price = price
        self.alcohol_content = alcohol_content
        self.volume = volume

    def __str__(self):
        return "{self.name}, ${self.price:.2f}, {self.volume}ml ({self.alcohol_content}%)".format(self=self)

    def get_alcohol_volume(self):
        return (self.alcohol_content / 100) * self.volume

    def is_alcoholic(self):
        # if self.alcohol_content >= 1:
        #     return True
        # else:
        #     return False
        return self.alcohol_content >= Drink.MINIMUM_ALCOHOL_THRESHOLD

def run_tests():
    # d1 = Drink()
    # print(d1)
    #
    d2 = Drink("Pina Colada", 12.3, 450, 12.5)
    d3 = Drink("Coffee", 4.5, 280, 0)
    # print(d2)



    total_alcohol = 0
    count_alcoholic_drinks = 0
    drinks = [d2, d2, d3]
    for drink in drinks:
        if drink.is_alcoholic():
            count_alcoholic_drinks += 1
            total_alcohol += drink.get_alcohol_volume()
    print("You drank {} drinks, ({} were alcololic for a total of {}ml alcohol)".format(len(drinks),count_alcoholic_drinks, total_alcohol))


if __name__ == '__main__':
    run_tests()