import main
import story
import player
import actions
import items

def start_game():
    player = player.Player()
    story = story.Story()

    while player.is_alive() and not story.is_completed():
        action = player.get_next_action()
        if action:
            result = actions.process_action(action, player, story)
            print(result)

if __name__ == '__main__':
    start_game()
