import glob, os
from classes.element import Element

class End(Element):
    def __init__(self):
        Element.__init__(self, 'E', "assets/end.png")
