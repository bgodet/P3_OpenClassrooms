import glob, os

# Class of the maze's elements
##############################

class Maze:
    pass
"""
	def __init__(self, character, traversable, location):
		self.character = character
		self.traversable = traversable
		self.location = location

	def __str__(self):
		return self.character
"""

class Corridor(Maze):
    pass
"""
    def __init__(self, char, location):
        Maze.__init__(self, char, True, location)
        self.item = item
        self.player = player
        self.guardian = guardian
"""
class Wall(Maze):
    pass
"""
    def __init__(self, char, location):
        Maze.__init__(self, char, False, location)
"""

class End(Maze):
    pass
"""
    def __init__(self, char, location):
        Maze.__init__(self, char, True, location)
        self.player = None
"""

class Guardian(Maze):
    pass
"""
    def __init__(self, char, location):
        Maze.__init__(self, char, True, location)
"""

class Item(Maze):
    pass
"""
    def __init__(self, char, location):
        Maze.__init__(self, char, True, location)
"""

class Player(Maze):
    pass
"""
    def __init__(self, char, location):
        Maze.__init__(self, char, False, location)
        self.inventory = []
"""

with open("/Users/ggodet/Documents/Lab/P3_OpenClassrooms/level/maze.txt", mode='r') as fp:
    strlist = [list(line.rstrip('\n')) for line in fp]
        # check si il y a une ligne
    if len(strlist) > 0:
    # On récupère les lignes
        for x in range(0, len(strlist)):
            # On récupère les colonnes
            for y in range(0, len(strlist[0])):
                # On instancie les classes
                if (strlist[x][y] == 'X'):
                    str[x][y] = Wall()
                elif (strlist[x][y] == 'G'):
                    str[x][y] = Guardian()
                elif (strlist[x][y] == 'E'):
                    str[x][y] = End()
                elif (strlist[x][y] == ' '):
                    str[x][y] = Corridor()
                elif (strlist[x][y] == 'P'):
                    str[x][y] = Player()

    print(strlist[0][0])

"""
filepath = '/Users/ggodet/Documents/Lab/P3_OpenClassrooms/level/maze.txt'
maze_list = []

with open (filepath) as fp: ## Attention FP = Fichier ouvert
    for cnt, line in enumerate(fp):
        line = []
        for character in line:
            # Check si l'on passe sur un 'X' = mur
            if (character == 'X'):
                wall = Wall()
                line.append(wall)
            # Check si l'on passe sur un 'G' = Guardien
            elif (character == 'G'):
                guardian = Guardian()
                line.append(guardian)
            # Check si l'on passe sur un 'E' = fin du jeu
            elif (character == 'E'):
                end = End()
                line.append(end)
            # Check si l'on passe sur un ' ' = couloir
            elif (character == ' '):
                corridor = Corridor()
                line.append(corridor)
            elif (character == 'P'):
                player = Player()
                line.append(player)
            maze_list.append(line)

print(maze_list[0][0])
"""