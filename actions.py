class Actions:
    def __init__(self):
        self.actions = {
            "look": self.look,
            "go": self.go,
            "take": self.take,
            "use": self.use,
            "inventory": self.inventory,
            "help": self.help
        }
    
    def look(self, player, args):
        if len(args) == 0:
            player.look_around()
        else:
            player.look_at(args[0])
    
    def go(self, player, args):
        if len(args) == 0:
            print("Go where?")
        else:
            player.go_to(args[0])
    
    def take(self, player, args):
        if len(args) == 0:
            print("Take what?")
        else:
            player.take(args[0])
    
    def use(self, player, args):
        if len(args) == 0:
            print("Use what?")
        else:
            player.use(args[0])
    
    def inventory(self, player, args):
        player.show_inventory()
    
    def help(self, player, args):
        print("Actions you can take:")
        for action in self.actions.keys():
            print(f"- {action}")
