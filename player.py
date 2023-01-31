class Player:
    def __init__(self):
        self.inventory = []
        self.stats = {
            "strength": 0,
            "intelligence": 0,
            "dexterity": 0
        }
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
        
    def display_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"- {item}")
