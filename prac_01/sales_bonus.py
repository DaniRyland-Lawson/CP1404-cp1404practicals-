"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

#user_sales = float(input("Please enter sales: $"))
#if user_sales < 1000:
#    user_sales_bonus = user_sales * 0.1
#else:
#    user_sales_bonus = user_sales * 0.15
#print("Your bonus is: $", user_sales_bonus)

user_sales = float(input("Please enter sales: $"))
while user_sales >= 0:
    if user_sales < 1000:
        user_sales_bonus = user_sales * 0.1
    else:
        user_sales_bonus = user_sales * 0.15
print("Your bonus is: $", user_sales_bonus, sep='')
user_sales_bonus = float(input("Please enter sales: $"))
