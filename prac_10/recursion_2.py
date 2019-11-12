"""Recursion"""


def calculate_blocks(rows):
    if rows <= 0:
        return 0
    return rows + calculate_blocks(rows - 1)


def build_pyramid():
    chosen_rows = int(input("How many rows would you like your pyramid to be: "))
    print("For {} rows, you need {} blocks".format(chosen_rows, calculate_blocks(chosen_rows)))


build_pyramid()
