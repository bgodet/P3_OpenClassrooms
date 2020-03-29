import glob, os

class Player(Board):
    def __init__(self, char, location):
        Board.__init__(self, char, False, location)
        self.inventory = []
