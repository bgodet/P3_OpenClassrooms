from classes.element import Element
import glob, os

class End(Element):
    def __init__(self):
        Element.__init__(self, 'E', "assets/end.png")
