import glob, os
from classes.wall import *
from classes.corridor import *
from classes.end import *
from classes.guardian import *
from classes.player import *


# Class of the maze's elements
##############################

class Maze:

	def __init__(self, filepath):
		self.filepath = filepath

		# Fonction d'instencification des objets de mon labyrinthe
		##########################################################

		maze_list = []

		with open (filepath) as fp: # Attention FP = Fichier ouvert
			line = []
			for line in enumerate(fp):
				for character in line:
					# Check si l'on passe sur un 'X' = mur
					if (character == 'X'):
						line.append(Wall())
					# Check si l'on passe sur un 'G' = Guardien
					elif (character == 'G'):
						line.append(Guardian())
					# Check si l'on passe sur un 'E' = fin du jeu
					elif (character == 'E'):
						line.append(End())
					# Check si l'on passe sur un ' ' = couloir
					elif (character == ' '):
						line.append(Corridor())
					# Check si l'on passe sur un 'P' = joueur
					elif (character == 'P'):
						line.append(Player())
					# Ajout en mémoire de la line
					maze_list.append(line)

	# Fonction magique d'affichage
	##############################

	def __str__(self):
		
		for Maze.line in Maze.maze_list:
			for objet in Maze.line:
				if (objet == Wall()):
					Wall() = 'X'
				elif (objet == Guardian()):
					Guardian() = 'G'
				elif (objet == End()):
					End() = 'E'
				elif (objet == Corridor()):
					Corridor() = ' '
				elif (objet == Player()):
					Player() == 'P'

	# Probleme suivant : Ne se concatène pas
	# ! NE FONCTIONNE PAS POUR LE MOMENT ! #
