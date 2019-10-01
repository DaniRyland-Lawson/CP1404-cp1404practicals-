"""CP1404 Programming II
Test to see of UnreliableCar class works."""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test for UnreliableCars."""

    # Create some cars for reliability
    good_car = UnreliableCar("Good Car", 100, 80)
    bad_car = UnreliableCar("Bad Car", 100, 10)

    # Attempts to drive the cars multiple times
    # Output is what the drove in kms
    for i in range(1, 10):
        print("Attempting to drive {}km: ".format(i))
        print("{:10} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:10} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)


main()
