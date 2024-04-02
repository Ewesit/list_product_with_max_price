def find_highest_priced_product(products):
    highest_priced_product = None #checks if highest priced product is none.
    highest_price = None  #checks if highest price is none
    for product in products:
        #check if the value of the current product is higher than the 'highest_price'
        if highest_price is None or product['price'] > highest_price:
            highest_price = product['price']
            highest_priced_product = product
    return highest_priced_product

# list dictionaries called products
products = [
    {'name': 'Rice', 'price': 100},
    {'name': 'Sugar', 'price': 200},
    {'name': 'Cooking oil', 'price': 180},
    {'name': 'Unga', 'price': 200}
]
# Call find_highest_priced_product function with the products list as an argument
#find_highest_priced_product function is expected to return the dictionary representing
# the product with the highest price. 
#The result is assigned to the highest_priced_product variable.
highest_priced_product = find_highest_priced_product(products)
print(highest_priced_product)

