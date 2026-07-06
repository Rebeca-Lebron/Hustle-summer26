# Rebeca | Lab 4 | Intro to Python |

# Ticket 1 

ages = [17, 11, 25, 13, 9]

for item in ages:
    if item >= 13:
        print(" access granted")
    else:
        print("Too young")
          # 17 acess granted 
          # 11 too young
          # 25 access granted
          # 13 access granted 
          # 9 too young


 
# separted acceass granted and too young and keep checking into different lists

# Ticket 2



# set up a control variable
keep_checking = "yes"

while keep_checking == "yes":
    age = int(input("enter your age: ")) 
    if age >= 13:
        print("acess granted")
    else: 
        print ("too young")

    keep_checking = input("do you want to check another age? (yes/no): ")

