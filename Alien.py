from abc import ABC, abstractmethod
import logging


class Alien(ABC):
    """
    Abstract base class for aliens
    """

    def __init__(self):
        """
        Set the armor each alien has at the beginning to 2
        """
        self.armor = 2
        logging.info(f"{self} created")

    def __repr__(self):
        """
        Overwrite how an alien is represented in the play field when printing it
        :return:
        """
        return self.__str__()

    @abstractmethod
    def __str__(self):
        """
        Define how an alien is represented as a string
        :return: A string representation of the alien
        """
        pass

    @abstractmethod
    def got_hit(self):
        """
        Defines what happens when an alien is hit by a shot
        :return: True if the alien is dead (armor <= 0), False if armor is left
        """
        pass
