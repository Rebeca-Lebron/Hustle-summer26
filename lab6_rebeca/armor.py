import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_block = random.randint(0, self.max_block)
        print(random_block)
        return (random_block)

      
if __name__ == "__main__":
    my_armor = Armor("Steel Shield", 50)
    print(my_armor.name)
    print(my_armor.max_block)
    my_armor.block()