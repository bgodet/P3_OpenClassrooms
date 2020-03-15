import glob, os

class Map:
	# Ajout du fichier dans le constructeur de la map
	def __init__(self, fichier):
		self.fichier = 'map.txt'
		level = []
		# Lecture du fichier du niveau
		for filepath in glob.glob(fichier):
			# File readline à modifier en tableau 2D
			with open(filepath, "a+", encoding= 'utf-8') as file:
				lvl = []
				for line in file:
					lvl.append(line)
				level.append(lvl)
		# Gestion de la console et de l'affichage
		for line in level :
			print(line)
