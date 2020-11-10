import glob
import os
import random
from classes.wall import Wall
from classes.corridor import Corridor
from classes.end import End
from classes.guardian import Guardian
from classes.player import Player
from classes.item import Item, Needle, Tube, Ether

class Maze:
	"""
	
	"""
	##########################
	# Creating the constructor
	##########################

	def __init__(self, filepath):
		self.__maze_list = []
		self.__player = None
		self.__nbItem = 0

		#######################
		# Variables declaration
		#######################

		nbCorridor = 0
		nbPlayer = 0
		nbEnd = 0
		nbGuardian = 0

		#####################
		# Initialing the maze
		#####################

		if os.path.isfile(filepath):
			# Open file
			with open(filepath) as fp:
				# For each line on the  text file
				for x, line in enumerate(fp):
					maze_line = []

					#################################
					# Getting lines element on memory
					#################################

					for y, character in enumerate(line):
						if (character == 'X'):
							maze_line.append(Wall())
						elif (character == 'G'):
							maze_line.append(Guardian())
							nbGuardian += 1
						elif (character == 'E'):
							maze_line.append(End())
							nbEnd += 1
						elif (character == ' '):
							maze_line.append(Corridor())
							nbCorridor += 1
						elif (character == 'P'):
							self.__player = Player(x, y)
							maze_line.append(self.__player)
							nbPlayer += 1

					# Adding the line on memory
					if nbPlayer > 1:
						raise ValueError('Erreur : Votre niveau contient trop de joueurs !')
					elif nbGuardian > 1:
						raise ValueError('Erreur : Votre niveau contient trop de gardiens !')
					elif nbEnd > 1:
						raise ValueError('Erreur : Votre niveau contient trop de sorties')
					else:
						self.__maze_list.append(maze_line)

			################
			# Item placement
			################
 
			items = [Needle(),Tube(),Ether()]
			# With this attribute, the Maze already know how much items exist and how much is required
			self.__nbItem = len(items)
			randomCorridors = self.randomItem(len(items))

			if randomCorridors is not None:
				for i,(line,col) in enumerate(randomCorridors):
					self.__maze_list[line][col] = items[i]

		else:
			raise FileNotFoundError('Aucun fichier existant sur le chemin:' + filepath)

	def getMaze(self):
		return tuple(self.__maze_list)

	##################################
	# Display function for the console
	##################################

	def __str__(self):
		string = ""
		for row in self.__maze_list:
			for  item in row:
				string+=' {} '.format(item)
			string+='\n'
		return string

	def __repr__(self):
		return self.__str__()

	##################################
	# Function to place Items randomly
	##################################

	def randomItem(self, nbItems):
		nbLine = 0
		nbCorridors = []

		for line in self.__maze_list:
			nbColonne = 0
			for element in line:
				if isinstance(element, Corridor):
					nbCorridors.append((nbLine, nbColonne))
				nbColonne += 1
			nbLine += 1
		# Getting numbers of corridors
		if len(nbCorridors) >= nbItems :
			return random.sample(nbCorridors, nbItems)
		else:
			return None

	###################################
	# Core function for player movement
	###################################

	def __movePlayer(self, x, y):

		newX = self.__player.getX() + x
		newY = self.__player.getY() + y
		if (isinstance(self.__maze_list[newX][newY],Wall)):
			print("Impossible move.")

		# Adding items on the player condition
		# If the class is and Item
		elif (isinstance(self.__maze_list[newX][newY],Item)):
			item = self.__maze_list[newX][newY]
			# Adding items in the inventory list
			self.__player.addInventory(item)
			# Replace player element by a corridor
			self.__maze_list[self.__player.getX()][self.__player.getY()] = Corridor()
			self.__player.setX(newX)
			self.__player.setY(newY)
			# Set the new player position
			self.__maze_list[self.__player.getX()][self.__player.getY()] = self.__player
			print("You picked up " + item.description)

		# The game exit when player on the End cell
		elif (isinstance(self.__maze_list[newX][newY],End)):
			self.__maze_list[self.__player.getX()][self.__player.getY()] = Corridor()
			self.__player.setX(newX)
			self.__player.setY(newY)
			# Set the new player position
			self.__maze_list[self.__player.getX()][self.__player.getY()] = self.__player
			print("You getted out of the maze !")
			exit()

		elif (isinstance(self.__maze_list[newX][newY],Guardian)):
			if  self.__player.countInventory() != self.__nbItem:
				print("You LOOSE")
				exit()
			else:
				self.__maze_list[self.__player.getX()][self.__player.getY()] = Corridor()
				self.__player.setX(newX)
				self.__player.setY(newY)
				# Set the new player's position
				self.__maze_list[self.__player.getX()][self.__player.getY()] = self.__player
				print("You WIN")

		# Natural player moving
		else:
			self.__maze_list[self.__player.getX()][self.__player.getY()] = Corridor()
			self.__player.setX(newX)
			self.__player.setY(newY)
			self.__maze_list[self.__player.getX()][self.__player.getY()] = self.__player
	
	##############################
	# Function for player movement
	##############################

	def moveDown(self):
		self.__movePlayer(1,0)

	def moveUp(self):
		self.__movePlayer(-1,0)

	def moveLeft(self):
		self.__movePlayer(0,-1)

	def moveRight(self):
		self.__movePlayer(0,1)
