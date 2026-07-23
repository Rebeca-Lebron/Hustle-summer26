import random

# Step 2: Make a list of three distinct welcome messages
welcome_messages = [
    "Welcome to the shop! Happy shopping!",
    "Hello! Ready to find your next favorite item?",
    "Welcome back! Come and see your new favorite book or eredaers!"
]
# Step 3: Pick one random message from the list
random_greeting = random.choice(welcome_messages)

# Step 4: Print it out to the terminal
print(random_greeting)

# TICKET 2: Put an item on sale DO your set_price guard

# Step 1: Define the Item class with the set_price guard method
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, new_price):
        # The guard: refuses anything below zero
        if new_price < 0:
            print("Error: Price cannot be below zero!")
        else:
            self.price = new_price


# Step 2: Create an item and USE set_price to lower its price for a sale
# Create the original item
sale_item = Item("Bigme b7", 300)
print(f"Original price of {sale_item.name}: ${sale_item.price}")

# Call set_price to lower it (putting it on sale)
sale_item.set_price(250)  # Lowering the price to $250

# Print the sale announcement message with the new price
print(f" SALE ALERT! The {sale_item.name} is now on sale for only ${sale_item.price}! ")

# TICKET 3: Print the store menu
#   Use a for loop over store.items() to display numbers, names, and prices.

# (Example store dictionary linking numbers to item objects)
store = {
    1: Item("Bigme b7", 300),
    2: Item("Boox go color7", 350),
    3: Item("Twilight", 10)
}

print("\n--- STORE MENU ---")

# Use a for loop over store.items() to unpack the number and the item object
for number, item in store.items():
    # Wrap the price in str() to join it with the text string
    print(str(number) + ": " + item.name + " - $" + str(item.price))

# TICKET 4: Handle a wrong choice DO if / elif / else

print("\n--- Start Shopping ---")

# --- ADD THIS LINE BEFORE THE LOOP ---
cart = []  

while True:
    # Get the customer's raw text input
    choice = input("Enter an item number or type 'done' to finish: ")
    
    # 1. IF: check if they are finished shopping
    if choice.lower() == "done":
        print("Thank you for shopping! Proceeding to checkout...")
        break
        
    # 2. ELIF: convert input to an integer and check if it is a valid menu number
    elif choice.isdigit() and int(choice) in store:
        item_number = int(choice)
        selected_item = store[item_number]
        cart.append(selected_item)  # Assuming 'cart' is your items list
        print(f"-> Added {selected_item.name} to your cart!")
        
    # 3. ELSE: handle anything else that isn't on the menu
    else:
        print("Sorry, that's not on the menu!")


# TICKET 5: Print a receipt DO for loop · list

# 1. Print the receipt header
print("\n==============================")
print("       OFFICIAL RECEIPT       ")
print("==============================")

# 2. Use a for loop over the cart list to print each chosen item
if len(cart) == 0:
    print("No items purchased. Your cart was empty!")
else:
    for bought_item in cart:
        print(f"- {bought_item.name}: ${bought_item.price}")

print("==============================")

# TICKET 6: Count the order DO list

# 1. Calculate the total number of items bought using len()
item_count = len(cart)

# 2. Convert the count to a string using str() and print the sentence
print("You bought a total of " + str(item_count) + " things today!")
