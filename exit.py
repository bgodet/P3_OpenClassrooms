import glob, os

class Exit(Board):

    def __init__(self, char, location):
        Board.__init__(self, char, True, location)
        self.player = None