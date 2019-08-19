# These are Global
MIN_LENGTH = 6
MAX_LENGTH = 8

# This is used to print the astericks in place of the password.
def stars_print(sequence):
    return('*' * len(sequence))

def get_password(MIN_LENGTH, MAX_LENGTH):
    password = input("Can you please enter a valid password, between {} and {} characters long: " .format(MIN_LENGTH, MAX_LENGTH))
    if len(password) < MIN_LENGTH:
        print("Sorry your password is too short")
    if len(password) > MAX_LENGTH:
        print("Sorry your password is too Long")
    else:
        return password

def main():
    password = get_password(MIN_LENGTH, MAX_LENGTH)
    print(" Thank you, your password is: ", stars_print(password))

main()
