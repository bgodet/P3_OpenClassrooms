import glob
import os
from classes.wall import *
from classes.corridor import *
from classes.end import *
from classes.guardian import *
from classes.player import *

class Maze:

	def __init__(self, filepath):
		#self.filepath = filepath À remove.
		self.maze_list = []

		# Fonction d'instencification des objets
		########################################

		with open(filepath) as fp:  # Attention FP = Fichier ouvert
			for line in fp:
				maze_line = []
				for character in line:
					# Check si l'on passe sur un 'X' = mur
					if (character == 'X'):
						maze_line.append(Wall())
					# Check si l'on passe sur un 'G' = Guardien
					elif (character == 'G'):
						maze_line.append(Guardian())
					# Check si l'on passe sur un 'E' = fin du jeu
					elif (character == 'E'):
						maze_line.append(End())
					# Check si l'on passe sur un ' ' = couloir
					elif (character == ' '):
						maze_line.append(Corridor())
					# Check si l'on passe sur un 'P' = joueur
					elif (character == 'P'):
						maze_line.append(Player())
				# Ajout en mémoire de la line
				self.maze_list.append(maze_line)

	# Fonction d'affichage de la représentation mémoire des objets
	##############################################################

	def __str__(self):
		string = ""
		for row in self.maze_list:
			for item in row:
				string+=' {} '.format(item)
			string+='\n'
		return string

	def __repr__(self):
		return self.__str__()

	# return '\n'.join([''.join(['{}'.format(item) for item in row]) for row in self.maze_list])
	# return '\n'.join([''.join(str(row)) for row in self.maze_list])
