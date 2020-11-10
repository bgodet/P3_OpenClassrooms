from classes.element import *
import glob, os

class Wall(Element):
    def __init__(self):
        Element.__init__(self, 'X', "assets/wall.png")
