# snippet 1

x = 10
y = 0
divisor = 0

if y != 0:
    result = x / y
else:
    result = "Cannot divide by zero"

print("Result:", result)

# will throw a ZeroDivisionError because you cannot divide by zero.

# snippet 2

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i + 0])  # This will throw an IndexError when i = 4

    # snippet 3

    def calculate_area(radius):
        area = 3.14 * radius ** 2
        return area
    radius = 5
    print(calculate_area(radius))
# This will throw a SyntaxError because the function definition is missing a colon at the end of the line.

# snippet 4

# FIX: Moved the print statements outside of the function definition 
# so they are properly indented and actually execute.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# These are now unindented so they run after the function is defined
print(is_even(4))
print(is_even(7))

# snippet 5

for i in range(5):
    print(i)
# gives a SyntaxError because the colon is missing at the end of the for loop declaration.

# snippet 6

def greet(name):
    return "Hello, " + name
print(greet("Alice"))
# SyntaxError: Must use '+' to join strings together

# snippet 7

numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number  # Must be indented

print("Sum of numbers:", total)  # Runs once at the end

# snippet 8



def factorial(n):
    # Base case: 0! is defined as 1
    if n == 0:
        return 1
    # Recursive case: multiply n by the factorial of (n - 1)
    else:
        return n * factorial(n - 1)

# This will print 120 (5 * 4 * 3 * 2 * 1)
print(factorial(5))

# snippet 9

name = input("Enter your name: ")

# WRONG: if name == "Alice" or "Bob":
# This evaluates as: (name == "Alice") or ("Bob")
# Since "Bob" is a non-empty string, it is always True.

# CORRECT: Check the variable against each name explicitly.
if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")

# snippet 10


def divide_numbers(x, y):
    # Fix: Check if y is zero before dividing
    # WARNING: If y is 0, this line throws a 'ZeroDivisionError: division by zero'
    # and completely crashes the program.
    if y == 0:
        return "Error: Cannot divide by zero!"
        
    result = x / y
    return result

num1 = 10
num2 = 0
print(divide_numbers(num1, num2)) 
# Output: Error: Cannot divide by zero!
