from Player import Player


class HumanPlayer(Player):
    """
    A player that is steered by user inputs
    """

    def shoot(self):
        selection = int(input(f"Shooting at column(1-{self.cols}): "))
        if selection <= self.cols:
            return selection-1  # the player will choose 1-self.cols, hence return value must be selection-1
