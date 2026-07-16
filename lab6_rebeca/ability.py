import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_damage = random.randint(0, self.max_damage)
        print(random_damage)
        return (random_damage)

if __name__ == "__main__":
    my_ability = Ability("Super Strength", 100)
    print(my_ability.name)
    print(my_ability.max_damage)
    my_ability.attack()