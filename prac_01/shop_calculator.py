"""
Sales bonus program
"""

total_cost = 0
items = int(input("Please enter how many items: "))
while items <0:
    print ("Invalid number!")
    items = int(input("Please enter how many items: "))
for i in range (items):
    cost = float(input("What is the price of the item?: "))
    total_cost += cost

if total_cost > 100:
    total_cost *= 0.9

print("Total price for ", items, " items is $", total_cost, sep='')




