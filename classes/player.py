import glob, os
from classes.element import Element


class Player(Element):    
    """
    The Player class contain the inventory and the "x" and "y" positions for picking items and move through the maze.
    """
    def __init__(self, x, y):
        Element.__init__(self, 'P', "assets/mac_gyver.png")
        self.__x = x
        self.__y = y
        self.__inventory = []

    # Getter method to get the properties
    def getInventory(self):
        return tuple(self.__inventory)
    # Add items in the inventory
    def addInventory(self, element):
        self.__inventory.append(element)
    # Counter to know how many objects the player is carrying
    def countInventory(self):
        return len(self.__inventory)

    ############################################
    # Getters and Setters of the Player position
    ############################################

    # Getter method to get the properties
    def getX(self):
        return self.__x
    # Setter method to change the value
    def setX(self, x):
        self.__x = x
    # Getter method to get the properties
    def getY(self):
        return self.__y
    # Setter method to change the value
    def setY(self, y):
        self.__y = y
