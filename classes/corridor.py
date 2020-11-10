import glob, os
from classes.element import Element

class Corridor(Element):
    def __init__(self):
        Element.__init__(self, " ", "assets/corridor.png")
