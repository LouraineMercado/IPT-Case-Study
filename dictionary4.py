# Num 4 DICTIONARY
# Function to add products and prices to the dictionary
def add_products():
    products = {}  # Initialize an empty dictionary to store products and prices
    while True:
        product_name = input("Enter the product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break  # Exit the loop if the user is done entering products
        price = float(input("Enter the price of {}: $".format(product_name)))
        products[product_name] = price  # Add the product and price to the dictionary
    return products

# Function to retrieve price for a product
def retrieve_price(products):
    while True:
        product_name = input("Enter a product name to retrieve its price (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break  # Exit the loop if the user is done retrieving prices
        if product_name in products:
            print("Price of {}: ₱{}".format(product_name, products[product_name]))
        else:
            print("Product '{}' not found.".format(product_name))

# Main function to execute the program
def main():
    print("Add products and prices:")
    products = add_products()
    print("\nProduct list:", products)
    print("\nRetrieve product prices:")
    retrieve_price(products)

# Call the main function to start the program
main()
