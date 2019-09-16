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

# make CSV from list of lists
# with open("products.csv", "w") as output_file:
#     for product in products:
#         sale_status = 'y' if product[2] else 'n'
#         print("{}, {}, {}".format(product[0], product[1], sale_status))

PRODUCTS_FILE = "products.csv"
MENU_STRING = ">>>"

def main():
    print(MENU_STRING)
    menu_selection = input(">").upper()
    while menu_selection != "Q":
        if menu_selection == "L":
            print("list")
        elif menu_selection == "S":
            print("swap")
        else:
            print("Invalid")
        print(MENU_STRING)
        menu_selection = input(">").upper()
    print("Finished")





main()