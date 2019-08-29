#1 getting the numbers from the user

numbers = []
for i in range(5):
    user_number = int(input("Number: "))
    numbers.append(user_number)

print("The first number you have chosen is: ", numbers[0])
print("The last number you have chosen is: ", numbers[-1])
print("The smallest number you have chosen is ", min(numbers))
print("The largest number you have chosen is ", max(numbers))
print("The average out of the numbers you have chosen is ", sum(numbers) / len(numbers))

#Adding usernames to the mix
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = str(input("Please enter your username: "))

if username in usernames:
    print("Access granted.")
else:
    print("Access denied. ")
