import random

from Alien import Alien
from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer
from RecordedPlayer import RecordedPlayer
from WeakAlien import WeakAlien
from StrongAlien import StrongAlien
import copy
import logging
import datetime

logging.basicConfig(filename="alien_attack.log", level=logging.INFO)
current_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")


class Game:
    """
    A random number of aliens is placed at the top row of a play field.
    In each game iteration, a player can shoot at a column.
    If an alien is hit, its armor gets reduced based on the alien type
    If no armor is left, the alien is dead at disappears from the play field
    In each game iteration, all aliens move one row downwards
    If an alien comes to the ground (not the last row, but beyond it), the aliens win!
    If all aliens are shot before reaching the ground, the humans win!
    """

    def __init__(self, rows=10, columns=10, nr_aliens=5, ratio=0.5, mode="computer"):
        """
        Initializes the member variables, Generates a player based on the mode
        Calls the init_sky and init_aliens methods to init a valid game
        :param rows: Nr. of rows in the play field
        :param columns: Nr. of columns in the play field
        :param nr_aliens: Nr. of aliens to add
        :param ratio: the ratio between weak and strong aliens
        :param mode: the play mode: "computer" for computer player, "human" for human player
        """
        self.winner = None
        self.sky = []

        # init player
        self.mode = mode
        self.columns = columns
        self.rows = rows

        if self.mode == "computer":
            self.player = ComputerPlayer(self.columns)
        elif self.mode == "recorded":
            self.player = RecordedPlayer(self.columns)
        else:
            self.player = HumanPlayer(self.columns)

        # init sky and aliens
        self.init_sky()

        self.ratio = ratio
        self.init_aliens(nr_aliens, ratio)
        self.running = True

        logging.info(f"[{current_time}]: Game created\n"
                     f"Sky: {self.rows} × {self.columns}\n"
                     f"Number of aliens: {nr_aliens}\n"
                     f"Difficulty: {int((1 - self.ratio) * 100)}%\n"
                     f"Player: {self.mode}")

    def show(self):
        """
        prints the game
        """
        for r in self.sky:
            print(r)

    def init_sky(self):
        """
        Initialize the sky with empty fields
        """
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append("_")
            self.sky.append(row)

    @staticmethod
    def get_species(probability):
        """
        Returns either a StrongAlien or a WeakAlien.
        Hint: Use random.random to create a random value between 0 and 1
        :param probability: The probability to create a WeakAlien
        :return: the generated alien
        """
        if random.random() > probability:
            return StrongAlien()
        else:
            return WeakAlien()

    def init_aliens(self, nr_aliens, probability):
        """
        Initializes the aliens and places them randomly at the top row of the play field
        :param nr_aliens: The number of aliens to be generated
        :param probability: The probability to create a WeakAlien
        """
        spawned = 0
        while spawned < nr_aliens:
            index, choice = random.choice(list(enumerate(self.sky[0])))

            if choice == "_":
                self.sky[0][index] = self.get_species(probability)
                spawned += 1

    def play_one_round(self, column):
        """
        This is implementing the main game loop
        """
        # create a deep copy of the sky to work with
        tmp = copy.deepcopy(self.sky)

        # loop through self.sky and check for every alien you find

        # is it hit by a shot
        for row in tmp:
            if isinstance(row[column], Alien):
                row[column].got_hit()

        # elif it reached the ground, if so, the aliens won
        for column in range(self.columns):
            if repr(tmp[self.rows - 1][column]) != "'_'":
                print(f"Alien Won!")
                logging.critical(f"Aliens won the game\n - - - - - - -")
                self.winner = "Aliens"
                return True

        # else move it one row downwards
        tmp.insert(0, tmp.pop(self.rows - 1))

        # set the tmp play filed back to the real one
        self.sky = tmp

        # show the play filed
        self.show()

        # check if aliens remain, if not, humans won
        if not self.aliens_remain():
            print("Humans won!")
            logging.critical(f"{repr(self.mode)} won the game\n - - - - - - -")
            self.winner = "Humans"
            return True

        print("--------------")

    def play(self):
        while self.running:
            column = int(input("choose row: "))
            if self.play_one_round(column):
                break

    def aliens_remain(self):
        """
        Checks if some aliens remain at the sky
        :return: True if there are aliens left, False otherwise
        """
        for row in self.sky:
            for column in row:
                if repr(column) != "'_'":
                    return True
        return False


if __name__ == '__main__':
    game = Game(nr_aliens=1, mode="player")
    game.show()
    print()
    game.play()
