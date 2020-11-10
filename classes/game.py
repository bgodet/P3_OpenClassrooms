import pygame

from classes.maze import Maze
from classes.player import Player
from classes.guardian import Guardian
from classes.item import *
from classes.wall import Wall
from classes.corridor import Corridor
from classes.end import End
from classes.element import Element

class Game:
    def __init__(self):
        self.maze = Maze('level/maze.txt')
