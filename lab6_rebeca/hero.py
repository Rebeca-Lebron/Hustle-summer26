import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100): #starting_health=100 makes the starting_health arugument OPTIONAL
    
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def battle(self, opponent): #chooses a random winner between 2 heroes
        my_list = [self.name, opponent.name]
        print(random.choice(my_list))

    def add_ability(self, ability): # adds an ability to the hero's list of abilities
        self.abilities.append(ability)

    def add_armor(self, armor): # adds an armor to the hero's list of armors
        self.armors.append(armor)

    def attack(self):
        # Indent these lines by 4 spaces
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack() # adds an ability to hero's list of abilities
        return total_damage

    def take_damage(self, damage):
        blocked = self.defend()
        damage_taken = max(damage - blocked, 0)
        self.current_health -= damage_taken
        if self.current_health < 0:
            self.current_health = 0
            return damage_taken

    def defend(self):
        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block() # adds an armor to hero's list of armors
        return total_blocked

def battle(self, opponent):
    # Check if either hero lacks abilities
    if not self.abilities or not opponent.abilities:
        print("Draw")
        return

    # Start the fighting loop
    while self.current_health > 0 and opponent.current_health > 0:
        # Step 1: Execute simultaneous attacks
        self_attack_power = self.attack()
        opp_attack_power = opponent.attack()
        
        # Step 2: Apply mutual damage
        opponent.take_damage(self_attack_power)
        self.take_damage(opp_attack_power)
        
        # Step 3: Check for a winner
        if self.current_health <= 0 and opponent.current_health <= 0:
            print("Both heroes fell! It's a draw!")
            break
        elif opponent.current_health <= 0:
            print(f"{self.name} won!")
            break
        elif self.current_health <= 0:
            print(f"{opponent.name} won!")
            break

def attack(self):
    """ Calculate the total damage from all abilities and weapons. """
    total_damage = 0
    
    # Loop through every ability and weapon in the list
    for ability in self.abilities:
        # Call the attack method on each object and add it to the total
        total_damage += ability.attack()
        
    return total_damage


if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  my_hero = Hero("spider man", 150) #150 is our starting health
  #print(my_hero.name)
  #print(my_hero.current_health)
  #my_opponent = Hero("batman", 200)
  #my_hero.battle(my_opponent)
  # my_hero.add_ability(Ability("Web Shooter", 25))
  # my_hero.add_ability(Ability("Spidey Senses", 10))
  # my_hero.attack()
  my_hero.add_armor(Armor("Gloves", 5))
  my_hero.add_armor(Armor("A Really Cool Hat", 10))
  #my_hero.defend()
  my_hero.take_damage(10)

if __name__ == "__main__":
    hero = Hero("spider man", 100)
    # 2. Create a standard ability and add it
    # (Assuming Ability class takes name and max_damage)
    strike = Ability("Shield Bash", 20)
    hero.add_ability(strike)
    
    # 3. Create a weapon and add it
    excalibur = Weapon("Excalibur", 50)
    hero.add_weapon(excalibur)
    
    # 4. Test the combined attack power
    print(f"Total calculated attack damage: {hero.attack()}")
