#importing random numbers

import random

#GLOBAL
NUMBERS_IN_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    quick_pick_number = int(input("Please enter how many picks you would like?: "))
    while quick_pick_number <= 0:
        print("Invalid selection.")
        quick_pick_number = int(input("Please enter how many picks you would like?: "))

    for i in range(quick_pick_number):
        quick_picks = []
        for j in range(NUMBERS_IN_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()

        print(" ".join("{:2}".format(number) for number in quick_picks))

main()
#This one was very confusing to me. I had to look at the solution for this one. I was no where on track.