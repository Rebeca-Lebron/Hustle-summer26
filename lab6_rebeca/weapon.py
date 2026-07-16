 import random

class Weapon(Ability):
    def attack(self):
        """ Returns a random value between half of max_damage and full max_damage. """
        # Use integer division (//) to get a clean half-value
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)
