import glob, os

################################ 
# Class of the maze's elements #
################################

class Board:

	def __init__(self, character, passable, location):
		self.character = character
		self.passable = passable
		self.location = location

	def __str__(self):
		return self.character
