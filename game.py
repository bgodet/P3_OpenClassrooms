import glob, os
from classes.maze import *
from classes.wall import *
from classes.corridor import *
from classes.item import *
from classes.player import *
from classes.end import *
from classes.guardian import *

maze = Maze('/Users/ggodet/p3_openclassrooms/level/maze.txt')

print(maze)

# Pas de print !!!
# Recherche des erreurs de Pylint :
# No name 'item' in module 'classes'pylint(no-name-in-module) #
