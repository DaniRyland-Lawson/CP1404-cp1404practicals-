"""
CP1404/CP5632 Practical
Recursion
"""
import doctest


def do_it(n):
    """Do... it.
    >>> do_it(5)
    True
    >>> do_it(4)
    False"""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# False
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0.
    >>> do_something(4)
    True
    >>> do_something(3)
    False"""
    if n < 0:
        return 0
    print(n ** 2)
    do_something(n - 1)


# TODO: 3. write down what you think the output of do_something(4) will be,
# 0, 2, 4, 8, 16
# TODO: 4. use the debugger to step through and see what's actually happening
do_something(4)

# TODO: 5. fix do_something() so that it works according to the docstring


doctest.testmod()
