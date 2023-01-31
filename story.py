import random

class Story:
    def __init__(self, prompt, options):
        self.prompt = prompt
        self.options = options

    def generate_story(self):
        print(self.prompt)
        for option in self.options:
            print(f"{option[0]}. {option[1]}")
        choice = input("What do you want to do? Choose an option number: ")
        return int(choice)

    def next_story_node(self, choice):
        return self.options[choice - 1][2]
