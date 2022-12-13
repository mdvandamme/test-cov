"""
Observation
"""

class Obs:
    """Class to define an observation"""

    def __init__(self, pos):
        """
        :param position: A point coordinate
        """
        self.position = pos
        

    def __str__(self) -> str:
        """String of observation"""
        return (str)(self.position)

    def getElevation(self):
        """
        """
        return self.position[2]

    