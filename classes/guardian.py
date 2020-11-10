import glob, os
from classes.element import Element

class Guardian(Element):
    def __init__(self):
        Element.__init__(self, 'G', "assets/guardian.png")
