"""CP1404 Programming II demo program week 6 prac

0. Pattern based programming
1. Names based on problem domain
2. Functions at the same leve of abstraction( main should "look" the same

Menu- driven program
load products
- L_ist products
- S_wap sale status (get product number with error checking)
- Q_uit (save file)
"""

PRODUCTS_FILE = "products.csv"
MENU_STRING = ">>>"


def main():
    products = load_products()
    print(products)
    print(MENU_STRING)
    menu_selection = input(">").upper()
    while menu_selection != "Q":
        if menu_selection == "L":
            list_products(products)
        elif menu_selection == "S":
            swap_sale_status(products)
        else:
            print("Invalid")
        print(MENU_STRING)
        menu_selection = input(">").upper()
    save_products(products)
    print("Finished")


def load_products():
    print("loading")
    products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.50, True]]
    return products


def list_products(products):
    print("list")
    for product in products:
        print(product)


def swap_sale_status(products):
    list_products(products)
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input("? "))
            if number < 0:
                print("Product must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    print(products[number])


# make CSV from list of lists
def save_products(products):
    with open("products.csv", "r") as output_file:
        for product in output_file:
            sale_status = 'y' if product[2] else 'n'
            print("{}, {}, {}".format(product[0], product[1], sale_status))


main()
