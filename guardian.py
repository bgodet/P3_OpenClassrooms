import glob, os

class Guardian(Board):

    def __init__(self, char, location):
        Board.__init__(self, char, False, location)
