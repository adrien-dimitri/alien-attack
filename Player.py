from abc import ABC, abstractmethod
import logging


class Player(ABC):
    """
    Abstract Player class
    """

    def __init__(self, cols):
        """
        Constructor
        :param cols: the available columns of the play field
        """
        self.cols = cols
        logging.info(f"Mode: {type(self).__name__}")

    @abstractmethod
    def shoot(self):
        """
        Abstract method to shoot at a selected column
        :return: the column to shoot at
        """
        pass
