import glob, os

class map(object):


	levels = []

	# Ajout du fichier dans le constructeur de la map
	def __init__(self, fichier):
		mazeFolder = "./niveau"
		fichier = "maze.txt"

		# Lecture du fichier du niveau
		for filepath in glob.glob(ficher):
			# File readline à modifier en tableau 2D
			with open(filepath, "a+", encoding= 'utf-8') as file:
				lvl = []
				for line in file:
					lvl.append(line)
				levels.append(lvl)
		# Gestion de la console et de l'affichage
		for line in levels [0]:
			print(line)
