from Player import Player
import random


class ComputerPlayer(Player):
    """
    A player that is steered automatically by the computer
    """

    def __init__(self, cols):
        """
        Constructor which is initializing a memory
        The memory remembers how often the player already shot at each column
        :param cols:
        """
        super().__init__(cols)

        self.memory = []
        for i in range(cols):
            self.memory.append(0)
        # Init memory and set 0 for all columns

    def shoot(self):
        """
        Shoots smartly at a specific column
        :return:
        """
        # smartly select a column where it was not already shot 2 times at before
        # remember that it was shot at this column one more time in the memory

        input(f"\nPress ENTER to advance a round")
        while True:
            selection = random.randint(0, self.cols-1)
            if self.memory[selection] == 2:  # nothing happens if the column was chosen twice already,
                continue                     # and another selection is attempted
            else:
                for i in range(self.cols):
                    if i != selection:       # self.memory looks like [0,0,1,0,0... ]
                        self.memory[i] = 0   # every col's memory except selection is reset to zero
                self.memory[selection] += 1  # 1 is added to selected column's memory
                print(f"\nComputer shot at column {selection + 1}")  # +1 to print, player sees values from 1 to cols
                return selection



        # return the value