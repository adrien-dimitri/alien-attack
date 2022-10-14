from Alien import Alien


class WeakAlien(Alien):
    """
    A weak alien gets -2 on its armor when hit by a shot
    """

    def __str__(self):
        if self.armor > 0:
            return f"WA{self.armor}"
        else:
            return repr("_")

    def got_hit(self):
        self.armor -= 2
        return True

