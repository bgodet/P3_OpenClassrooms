import glob, os
from classes.element import Element

"""
Needle, Tube and Ether classes heritates from the Item attributes.
"""

class Item(Element):
    def __init__(self, character, image):
        Element.__init__(self, character, image)

class Needle(Item):
    def __init__(self):
        Item.__init__(self, '1', "assets/needle.png")
        self.description = "Needle"

class Tube(Item):
    def __init__(self):
        Item.__init__(self, '2', "assets/tube.png")
        self.description = "Plastic Tube"

class Ether(Item):
    def __init__(self):
        Item.__init__(self, '3', "assets/ether.png")
        self.description = "Bottle of Ether"
