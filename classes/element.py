import glob, os

"""
Mother class of the game for class heritage.
"""

class Element:
    def __init__(self, character, image):
        self.__character = character
        self.__image = image
    def __str__(self):
        return self.__character
    def __repr__(self):
        return self.__str__()
    def getCharacter(self):
        return self.__character
    def getImage(self):
        return self.__image
