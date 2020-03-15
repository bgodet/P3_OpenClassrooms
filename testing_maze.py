import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze")
wn.setup(700, 700)

#####################################################
## Création de la classe qui déssine le labyrinthe ##
#####################################################

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

# Création de la liste du niveau
levels = [""]

# Définition du labyrinthe
level_1 = [
"   ##### #  ###",
" #     # ## #  ",
"  ## #   #    #",
"#   ####   ####",
"   #     ###  #",
"## #### ##   ##",
"   ###    #####",
" #   ## # ##  #",
" ## #   #   ###",
"###  #### #####",
"### ## #  ##  #",
"#   #  # ##  ##",
"  ##  #     ###",
"##### ## ## ###",
"#    ###  #    "
]

levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            # Calcul des coordonnées
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check si le joueur est un mur
            if character == "#":
                pen.goto(screen_x, screen_y)
                pen.stamp()


# Création des instances
pen = Pen ()

# Mise en place du niveau
setup_maze(levels[1])

# Boucle du jeu
while True:
    pass
