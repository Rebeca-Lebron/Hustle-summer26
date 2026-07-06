# ============================================================
# LAB 5 - WEEK 5 : The VibeCheck Bug Hunt
# ============================================================
# Name: __________________
#
# This file is BROKEN on purpose. There are 8 bugs.
# Each one is marked with a # BUG comment and a number.
#
# Your job: fix every bug so the file runs with NO errors
# and prints the correct output (see the lab sheet).
#
# Read each error from the BOTTOM up. The last line names
# the error type. The line number tells you where to look.
#
# Fix ONE bug, run the file, then move to the next one.
# ============================================================


# ------------------------------------------------------------
# PART 1 - A function that greets a user
# ------------------------------------------------------------

# BUG 1: this function is missing something at the end of the line
def send_vibe():
    print("VibeCheck says: good energy only")


# BUG 2: the line inside this function is not indented
def welcome_user():
    print("Welcome to VibeCheck!")


# ------------------------------------------------------------
# PART 2 - A function that uses a variable
# ------------------------------------------------------------

def show_mood():
    mood = "hyped"
    # BUG 3: this uses a variable name that was never created
    print(f"Today's mood is {mood}")


# ------------------------------------------------------------
# PART 3 - A function with parameters
# ------------------------------------------------------------

def make_shoutout(name, mood):
    return f"{name} is feeling {mood} today!"


# ------------------------------------------------------------
# PART 4 - A function that counts hype points
# ------------------------------------------------------------

def count_hype(likes, shares):
    # BUG 4: this should ADD likes and shares, not subtract them
    total = likes + shares
    return total



# ============================================================
# RUNNING THE CODE - do not move these calls above the
# functions they use
# ============================================================

# BUG 5: fixed by separating the functions and placing the call after definitions.
def final_message():
    print("This is the final message!")  # (Or whatever final_message does)

def send_vibe():
    print("Sending good vibes!") 

# Move these calls BELOW the functions they use so Python can find them
welcome_user()
show_mood()
send_vibe()
final_message()



# BUG 6: make_shoutout returns a value, but nothing prints it.
# Wrap this call in a print() so the shoutout shows on screen.
print(make_shoutout("Jordan", "creative"))


# BUG 7: this passes only ONE value, but make_shoutout needs TWO
print(make_shoutout("Alex", "chill"))


# BUG 8: count_hype needs two numbers, but a word is being passed in.
# Change "ten" to a number so the math works.
print(count_hype(10, 5))


def final_message():
    print("Thanks for using VibeCheck!")

    # Add this at the very bottom of your file (with zero indentation)
final_message()
