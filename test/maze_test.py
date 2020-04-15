import turtle
import math
import random

# Maze properties
#################

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze")
wn.setup(700, 700)

# Maze Class
############

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

# Player class
##############

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

# Keyboard binding function
###########################

    def go_up(self):
        # Calculating the spot
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        # Wall checking
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # Calculating the spot
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        # Wall checking
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Calculating the spot
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        # Wall checking
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):

        # Calculating the spot
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        # Wall checking
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 5:
            return True
        else:
            return False

# Treasure class
################

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 1
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)   
        self.hideturtle()

# Creating the level list
levels = [""]

# Maze map
##########

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX          XXXXX",
"XT XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXXT       XX",
"XXXXXXT XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X TXXX        XXXXT XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX TXXXXXXXXXX         X",
"XXX                     X",
"XXX        TXXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX             TX",
"XX  TXXXXXXX            X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Adding the treasure list
treasures = []

levels.append(level_1)

# Graphic function
##################

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            # Calculating the coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is a X (representing the walls)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                # Add condition of the wall
                walls.append((screen_x, screen_y))

            # Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)
            # Check if it is a T (representing the treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

# Creating instences
pen = Pen()
player = Player()

# Wall list
walls = []

# Setup the level
setup_maze(levels[1])

# Keyboard settings
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

# Screen update
wn.tracer(0)

# Main loop
###########

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print ("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    # Update the screen
    wn.update()
