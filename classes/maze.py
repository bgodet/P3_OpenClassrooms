import glob
import os
import random
from classes.wall import *
from classes.corridor import *
from classes.end import *
from classes.guardian import *
from classes.player import *
from classes.item import *

class Maze:

	##########################
	# Création du constructeur
	##########################

	def __init__(self, filepath):
		self.__maze_list = []

		###################################
		# Déclaration des variables locales
		###################################

		nbLine = 0
		nbCharacterPerLine = 0
		nbCorridor = 0
		nbPlayer = 0
		nbEnd = 0
		nbGuardian = 0
		#nbItem = 0
		#nbFreeSpaces = []

		##############################
		# Initialisation du labyrinthe
		##############################

		if os.path.isfile(filepath):
			# Ouverture du fichier
			with open(filepath) as fp:
				# Pour chaque ligne du fichier
				for line in fp:
					maze_line = []
					nbLine += 1
					# Supression des \n pour vérifier l'égalité parfaite
					line = line.replace('\n','')
					# Nombre de caractère dans la line
					nbCharacterInLine = len(line)
					# Vérification des cas d'erreurs sur la ligne
					if nbLine == 1:
						nbCharacterPerLine = len(line)
					elif nbCharacterInLine != nbCharacterPerLine:
						raise ValueError('Votre labyrinthe n\'est pas carré')

					#################################################
					# Récupération des éléments des lignes en mémoire
					#################################################

					for character in line:
						nbCol = 0
						# Check si l'on passe sur un 'X' = mur
						if (character == 'X'):
							maze_line.append(Wall())
						# Check si l'on passe sur un 'G' = Guardien
						elif (character == 'G'):
							maze_line.append(Guardian())
							nbGuardian += 1
						# Check si l'on passe sur un 'E' = fin du jeu
						elif (character == 'E'):
							maze_line.append(End())
							nbEnd += 1
						# Check si l'on passe sur un ' ' = couloir
						elif (character == ' '):
							#nbItem += 1
							#nbFreeSpaces.append((nbLine, nbCol))
							maze_line.append(Corridor())
							nbCorridor += 1
						# Check si l'on passe sur un 'P' = joueur
						elif (character == 'P'):
							maze_line.append(Player())
							nbPlayer += 1
						#nbCol += 1
					#item1, item2, item3 = random.sample(nbFreeSpaces, 3)

					# Ajout en mémoire de la line
					if nbPlayer > 1:
						raise ValueError('Erreur : Votre niveau contient trop de joueurs !')
					elif nbGuardian > 1:
						raise ValueError('Erreur : Votre niveau contient trop de gardiens !')
					elif nbEnd > 1:
						raise ValueError('Erreur : Votre niveau contient trop de sorties')
					else:
						self.__maze_list.append(maze_line)
						
			# Vérification des cas d'erreurs sur le labyrinthe
			if nbLine < 4:
				print("Erreur : Le niveau du Labyrinthe est trop petit !\n")
		else:
			raise FileNotFoundError('Aucun fichier existant sur le chemin:' + filepath)

	##############################################################
	# Fonction d'affichage de la représentation mémoire des objets
	##############################################################

	def __str__(self):
		string = ""
		for row in self.__maze_list:
			for item in row:
				string+=' {} '.format(item)
			string+='\n'
		return string

	def __repr__(self):
		return self.__str__()
