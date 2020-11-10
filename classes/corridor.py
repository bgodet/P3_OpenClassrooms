from classes.element import Element
import glob, os

class Corridor(Element):
    def __init__(self):
        Element.__init__(self, " ", "assets/corridor.png")
