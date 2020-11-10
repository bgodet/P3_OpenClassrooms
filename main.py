import pygame
pygame.init()


from classes.game import Game

###############
# Main function
###############

def main():

    """
    The Main function using PyGame contain the main loop.
    The DisplayGraph method is used to display each images from classes.
    """

    pygame.display.set_caption("Aidez MacGyver à s'échapper !")
    screen = pygame.display.set_mode((600, 600))

    # Game generation
    start = True
    displayDic = {}
    game = Game()

    def displayGraph(maze):
        """
        For each element on the maze the function try to blit the image from the character key.
        If it can not, the except load the image and try to blit again.
        """
        nbLine = 0
        for line in maze:
            nbCol = 0
            for element in line:
                position = [nbCol * 40, nbLine * 40]
                try:
                    screen.blit(displayDic[element.getCharacter()], position)
                except:
                    displayDic[element.getCharacter()] = pygame.image.load(element.getImage())
                    screen.blit(displayDic[element.getCharacter()], position)
                nbCol += 1
            nbLine += 1
        # display update
        pygame.display.flip()

    # Game loop
    while start:
        """
        For each key event "up", "down", "right" or "left", the moving function is called. 
        """
        # Display the game
        displayGraph(game.maze.getMaze())
        for event in pygame.event.get():
            # Quit game condition
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
                print("Quit the game")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.maze.moveUp()
                    print("move up")
                elif event.key == pygame.K_DOWN:
                    game.maze.moveDown()
                    print("move down")
                elif event.key == pygame.K_RIGHT:
                    game.maze.moveRight()
                    print("move right")
                elif event.key == pygame.K_LEFT:
                    game.maze.moveLeft()
                    print("move left")

if __name__ == "__main__":
    main()
