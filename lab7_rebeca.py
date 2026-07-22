# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: rebeca__________________
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: Books ereaders_________________________________________
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.

# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: The program will print an error message instead of changing the price to -5.
#   Paste the message you see here: Error: Price cannot be below zero!

# TICKET 5: Each item's own action 
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: This is called polymorphism. Python looks at the type of object calling the method and runs the specific version defined inside that object's class.



class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, new_price):
        # Check if the price is valid
        if new_price < 0:
            print("Error: Price cannot be below zero!")
        else:
            self.price = new_price

    def use(self):
        print(f"Using the generic item: {self.name}.")

    # --- ADDED THIS METHOD SO TICKET 9 WORKS ---
    def deliver(self):
        print(f"{self.name} has been delivered!")


# TICKET 4: A second kind of item
class Book(Item):
    def __init__(self, name, price, author):
        # Super copies 'name' and 'price' setups from the original Item class
        super().__init__(name, price)
        self.author = author  # New specific attribute for Books

    def use(self):
        print(f"Reading '{self.name}' written by {self.author}.")

    # Books can have their own custom delivery style too!
    def deliver(self):
        print(f"The book '{self.name}' by {self.author} has been shipped out!")

# CHALLENGE: A third kind of item (Ereader)
class Ereader(Item):
    def __init__(self, name, price, model_version):
        super().__init__(name, price)
        self.model_version = model_version  # Specific attribute for Ereaders

    def use(self):
        print(f"Powering on your {self.name} ({self.model_version}). Time to read!")

    def deliver(self):
        print(f"Digital Delivery: An activation link for your {self.name} has been emailed!")



# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: Book
item_a = Item("Ereaders", 350)
item_b = Item("Chocolate", 10)
item_c = Item("Headphones", 150)


# =========================================================
# RUNNING ALL THE TESTS IN ORDER
# =========================================================

print("--- Testing Ticket 3: Validation ---")
item1 = Item("Book", 15)
print("Original price:", item1.price)

# 2. Try to break it with a negative number
item1.set_price(-5)
print("Price after invalid update:", item1.price)

# 4. Test a valid update just to be sure
item1.set_price(20)
print("Price after valid update:", item1.price)


print("\n--- Testing Ticket 4: Inheritance ---")
# 1. Create a book item
book1 = Book("The Great Gatsby", 12, "F. Scott Fitzgerald")
print(f"Book created: {book1.name} by {book1.author}, Price: {book1.price}")

# 2. Test if the inherited validation still works
print("\nTesting validation on Book class:")
book1.set_price(-10)
print("Book price after invalid update:", book1.price)


print("\n--- Testing Ticket 5: Polymorphism Actions ---")
# Testing the generic item action
item1.use()  

# Testing the custom book action
book1.use()  


print("\n--- TICKET 2: Verified Items ---")
# Printing your custom items to verify they work
print(f"Created: {item_a.name} (${item_a.price})")
print(f"Created: {item_b.name} (${item_b.price})")
print(f"Created: {item_c.name} (${item_c.price})")


# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================
# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.

class Cart:
   def __init__(self):
       self.items = []  # Holds the items in a list

   def add_item(self, item):
       self.items.append(item)

   # TICKET 9: Checkout  (add this method INSIDE your Cart class)
   #   Deliver every item and add up the total.
   def checkout(self):
       total = 0
       for item in self.items:
           item.deliver()  # Deliver every item safely now!
           total += item.price  # Add up the total
      
       self.items.clear()  # Clear the cart after checkout
       return total


# ==========================================
# CODE TO MAKE IT PRINT IN YOUR TERMINAL
# ==========================================

# 1. Create a cart instance
my_cart = Cart()

# 2. Add items to your cart
my_cart.add_item(item_a)  # Ereaders
my_cart.add_item(book1)   # The Great Gatsby Book

# 3. Print Ticket 6: Show that the cart is holding items
print("\n--- TICKET 6: Items currently inside the cart ---")
for current_item in my_cart.items:
   print(f"- {current_item.name}: ${current_item.price}")

# 4. Print Ticket 9: Run the checkout process
print("\n--- TICKET 9: Processing Checkout ---")
order_total = my_cart.checkout()
print(f"Final Receipt Total: ${order_total}\n")


# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.

# 1. Create the menu dictionary linking numbers to your real items
menu = {
   1: item_a,  # Ereaders
   2: item_b,  # Chocolate
   3: item_c,  # Headphones
   4: book1    # The Great Gatsby Book
}

# 2. Create one fresh, empty cart for the customer
customer_cart = Cart()

# 1. Create the menu dictionary linking numbers to your real items
menu = {
   1: item_a,  # Ereaders
   2: item_b,  # Chocolate
   3: item_c,  # Headphones
   4: book1    # The Great Gatsby Book
}

# 2. Create one fresh, empty cart for the customer
customer_cart = Cart()


# --- ADD THIS TO MAKE TICKET 7 PRINT IN YOUR TERMINAL ---
print("\n--- TICKET 7: Store Menu ---")
for number, item in menu.items():
   print(f"[{number}] {item.name} - ${item.price}")
   

# Create a real Ereader instance for the challenge
challenge_ereader = Ereader("Kindle Paperwhite", 140, "Generation 12")

# Update your Ticket 7 Menu to include it!
menu = {
    1: challenge_ereader,  # Challenge Item!
    2: item_b,             # Chocolate
    3: item_c,             # Headphones
    4: book1               # The Great Gatsby Book
}

# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: It will look up key 1 in the menu dictionary, find the Ereaders item, and add it to the customer's cart.

print("\n--- TICKET 8: Welcome to the Shop! ---")

while True:
   # 1. Ask the customer for their choice
   choice = input("Enter an item number to add to your cart, or type 'done' to checkout: ")
  
   # 2. Check if they want to stop shopping
   if choice.lower() == 'done':
       break
      
   # 3. Convert input to an integer to look it up in the menu dictionary
   try:
       item_number = int(choice)
      
       if item_number in menu:
           selected_item = menu[item_number]
           customer_cart.add_item(selected_item)  # Add it to the cart
           print(f"-> Added {selected_item.name} to your cart!")
       else:
           print("Invalid number! Please pick a number from the menu.")
          
   except ValueError:
       print("Please enter a valid number or 'done'.")

# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.
#
#   PREDICT the full output: The program will print out a final receipt showing that each item selected in Ticket 8 is delivered, followed by the combined dollar total of all those items.

print("\n--- TICKET 10: Final Checkout Receipt ---")

# 1. Check if the cart has anything in it before running checkout
if len(customer_cart.items) == 0:
   print("Your cart is empty! You didn't buy anything.")
else:
   # 2. Run your Ticket 9 checkout method on the customer's actual cart
   final_total = customer_cart.checkout()
   print(f"=====================================")
   print(f"GRAND TOTAL PAID: ${final_total}")
   print(f"=====================================\n")



# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================
