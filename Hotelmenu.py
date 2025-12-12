menu = {
    'Pizza': 40,
    'Burger': 25,
    'Pasta': 30,    
    'Salad': 15,
    'Dessert': 10,
    'Coffee': 50,
}

print("Welcome to the python Hotel!")
print("Pizza: $40\nBurger: $25\nPasta: $30\nSalad: $15\nDessert: $10\nCoffee: $50")

order_total = 0
items_ordered = []  # To keep track of ordered items

# First item
item_1 = input("Please enter the first item you would like to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    items_ordered.append(item_1)
    print(f"Your Item {item_1} has been added to your order")
else:
    print("Sorry, we don't have that item.")
    # Ask for another item immediately since first wasn't found
    another_item = input("Would you like to order something else? (Yes/No) ")
    if another_item.lower() == 'yes':
        item_2 = input("Please enter an item you would like to order: ")
        if item_2 in menu:
            order_total += menu[item_2]
            items_ordered.append(item_2)
            print(f"Item {item_2} has been added to your order")
        else:
            print(f"Item {item_2} is not available")

# Ask if user wants to add MORE items (regardless of what happened before)
add_more = input("Would you like to add another item to your order? (Yes/No) ")

while add_more.lower() == 'yes':
    item = input("Please enter the item you would like to add: ")
    if item in menu:
        order_total += menu[item]
        items_ordered.append(item)
        print(f"Item {item} has been added to your order")
    else:
        print(f"Sorry, {item} is not available in our menu.")
    
    add_more = input("Would you like to add another item? (Yes/No) ")

# Final order summary
print("\n=== Order Summary ===")
for item in items_ordered:
    print(f"{item}: ${menu[item]}")
print(f"Total Amount: ${order_total}")
print("Thank you for your order!")