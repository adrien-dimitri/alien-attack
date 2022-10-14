from Alien import Alien


class StrongAlien(Alien):
    """
    A strong alien gets -1 on its armor when hit by a shot
    """

    def __str__(self):
        if self.armor > 0:
            return f"SA{self.armor}"
        else:
            return repr("_")

    def got_hit(self):
        self.armor -= 1
        if self.armor < 0:
            return True
        return False
