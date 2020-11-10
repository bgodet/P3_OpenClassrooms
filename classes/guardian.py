from classes.element import Element
import glob, os

class Guardian(Element):
    def __init__(self):
        Element.__init__(self, 'G', "assets/guardian.png")
