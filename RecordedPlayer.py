import sys

from Player import Player

try:
    with open("recorded_game", "r") as file:
        col_list = [int(i) for i in file.read().split()]
except OSError:
    print("Could not open/read file:", "recorded_game")
    sys.exit()


class RecordedPlayer(Player):
    def shoot(self):
        input(f"\nPress ENTER to advance a round")
        selection = col_list.pop(0)
        print(f"Selected column: {selection+1}")
        return selection
