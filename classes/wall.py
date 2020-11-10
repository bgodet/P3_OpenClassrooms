import glob, os
from classes.element import *

class Wall(Element):
    """
    Wall class.
    """
    def __init__(self):
        Element.__init__(self, 'X', "assets/wall.png")
