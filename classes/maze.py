import glob, os
from wall import *
from corridor import *
from end import *
from guardian import *
from player import *

# Class of the maze's elements
##############################

class Maze:

	def __init__(self, character, filepath):
		self.character = character
		self.filepath = filepath

	# Fonction d'instencification des objets de mon labyrinthe
	##########################################################

	filepath = '/Users/ggodet/p3_openclassrooms/level/maze.txt'
	maze_list = []

	with open (filepath) as fp: # Attention FP = Fichier ouvert
		line = []
		for line in enumerate(fp):
			for character in line:
				# Check si l'on passe sur un 'X' = mur
				if (character == 'X'):
					wall = Wall('X')
					line.append(wall)
				# Check si l'on passe sur un 'G' = Guardien
				elif (character == 'G'):
					guardian = Guardian('G')
					line.append(guardian)
				# Check si l'on passe sur un 'E' = fin du jeu
				elif (character == 'E'):
					end = End('E')
					line.append(end)
				# Check si l'on passe sur un ' ' = couloir
				elif (character == ' '):
					corridor = Corridor(' ')
					line.append(corridor)
				elif (character == 'P'):
					player = Player('P')
					line.append(player)
				maze_list.append(line)

	print(maze_list)
"""

Cas d'erreur a gerer :

En sortie standard j'obtiens :

[(0, 'XXXXXXXXXXXXXXX\n'),
(0, 'XXXXXXXXXXXXXXX\n'),
(1, 'XPX  XXXXXX   X\n'),
(1, 'XPX  XXXXXX   X\n'),
(2, 'X X X     X X X\n'),
(2, 'X X X     X X X\n'),
(3, 'X X   XXX X X X\n'),
(3, 'X X   XXX X X X\n'),
(4, 'X XXX XX  X X X\n'),
(4, 'X XXX XX  X X X\n'),
(5, 'X   X  X XX X X\n'),
(5, 'X   X  X XX X X\n'),
(6, 'XXX XX X X  X X\n'),
(6, 'XXX XX X X  X X\n'),
(7, 'X X  X X X  X X\n'),
(7, 'X X  X X X  X X\n'),
(8, 'X X    X X  X X\n'),
(8, 'X X    X X  X X\n'),
(9, 'X XXXXXX X  X X\n'),
(9, 'X XXXXXX X  X X\n'),
(10, 'X X X    X  X X\n'),
(10, 'X X X    X  X X\n'),
(11, 'X X      X  X X\n'),
(11, 'X X      X  X X\n'),
(12, 'X X  XXXXX  XGX\n'),
(12, 'X X  XXXXX  XGX\n'),
(13, 'X           XEX\n'),
(13, 'X           XEX\n'),
(14, 'XXXXXXXXXXXXXXX'),
(14, 'XXXXXXXXXXXXXXX')]

Je ne devrai pas obtenir ce resultat le resultat attendu etant charactere par charactere ici c'est ligne par ligne.
"""
