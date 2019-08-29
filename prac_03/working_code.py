MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

#This program is to convert temperatures from Celsius to fahrenheit and vice versa.
def main():
    print(MENU)
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif user_choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("You have selected an invalid option.")
        print(MENU)
        user_choice = input(">>> ").upper()

# This function takes in the users_choice with Fahrenheit and converts to Celsius.
def convert_fahrenheit(fahrenheit):
     return 5/ 9 * (fahrenheit - 32)

# This function takes in the users_choice with celsius and converts to fahrenheit.
def convert_celsius(celsius):
    return celsius * 9.0 / 5 + 32

main()