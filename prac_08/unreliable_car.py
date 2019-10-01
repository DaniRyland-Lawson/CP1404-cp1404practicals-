""" CP1404 Programming II - New class for Unreliable car """
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.reliability = 0

    def drive(self, distance):
        random_number = randint(0, 101)
        if random_number < self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven