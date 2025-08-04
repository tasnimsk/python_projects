import pygame
import os
from grid import Grid

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (400, 100)
surface = pygame.display.set_mode([1050,900]) #the size of the whole window
#each cell will be 80x80
pygame.display.set_caption("Tasnim's Sudoku Game") #sets the title of the window

pygame.font.init()
gameFont = pygame.font.SysFont('Calibri', 50)
#for welcome page
titleFont = pygame.font.SysFont('Cambria', 80)
instructionFont = pygame.font.SysFont('Cambria', 30)

grid = Grid(pygame, gameFont)
running = True
gameActive = False #tracks if we're in the game or welcome page

def drawWelcomePage():
    surface.fill((214, 130, 152))

    welcomeSurface = titleFont.render("Welcome to Tasnim's Sudoku", True, (94,60,88))
    welcomeRect = welcomeSurface.get_rect(center=(525, 300))
    surface.blit(welcomeSurface, welcomeRect)

    instructionSurface = instructionFont.render("Press ENTER to start", True, (94,60,88))
    instructionRect = instructionSurface.get_rect(center=(525, 400))
    surface.blit(instructionSurface, instructionRect)

while running:

    #check for input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if gameActive: #only processes game events if game is active
            if event.type == pygame.MOUSEBUTTONDOWN and not grid.win:
                if pygame.mouse.get_pressed()[0]: # check for the left mouse button
                    pos = pygame.mouse.get_pos()
                    grid.getMouseClick(pos[0], pos[1])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and grid.win:
                    grid.restart()
        else: #welcome screen events
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                gameActive = True

    if gameActive:
        #window surface background color is mute pink
        surface.fill((214, 130, 152))

        #draw the grid here
        grid.draw(pygame, surface)

        #check if all cells were filed in accordance to the test grid
        if grid.win:
            wonFont = pygame.font.SysFont('Cambria', 50)
            wonSurface = wonFont.render("You Won!", False, (0,255,0))
            surface.blit(wonSurface, (830, 430))

            wonFont2 = pygame.font.SysFont('Cambria', 25)
            pressSpaceSurface = wonFont2.render("Press Space to restart", False, (94,60,88))
            surface.blit(pressSpaceSurface, (815, 500))
    else:
        drawWelcomePage()

    #update the window surface
    pygame.display.flip()
