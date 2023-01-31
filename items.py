class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f"{self.name}: {self.description}"
        
class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage
        
    def __str__(self):
        return f"{super().__str__()} ({self.damage} damage)"
        
class HealingItem(Item):
    def __init__(self, name, description, healing_amount):
        super().__init__(name, description)
        self.healing_amount = healing_amount
        
    def __str__(self):
        return f"{super().__str__()} ({self.healing_amount} healing)"
