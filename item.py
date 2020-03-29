import glob, os

class Item(Board):

    def __init__(self, char, location):
        Board.__init__(self, char, True, location)
