""" Write a list comprehensipn to product a new list
(True means it's on sale) """

products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.50, True]]
print(products)

on_sale_products = [product for product in products if product[2]]
print(on_sale_products)
print(sum([product[1] for product in products if product[2]]))
