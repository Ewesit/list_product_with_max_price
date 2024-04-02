def find_highest_priced_product(products):
    highest_priced_product = None
    highest_price = float('-inf')
    for product in products:
        if product['price'] > highest_price:
            highest_price = product['price']
            highest_priced_product = product
    return highest_priced_product

# Example usage
products = [
    {'name': 'Rice', 'price': 100},
    {'name': 'Sugar', 'price': 200},
    {'name': 'Cooking oil', 'price': 250},
    {'name': 'Unga', 'price': 200}
]
highest_priced_product = find_highest_priced_product(products)
print(highest_priced_product)
