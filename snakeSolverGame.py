import pygame
import pygame_menu
import time
import random

pygame.init()
# Menu Surface
surface = pygame.display.set_mode((400, 400))

# Snake Game Definitions
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
 
displayWidth = 400
displayHeight = 400
 
dis = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('JSIPs Snake')
 
clock = pygame.time.Clock()
 
snakeBody = 10
snakeSpeed = 20
 
gameFont = pygame.font.SysFont(None, 25)
scoreFont = pygame.font.SysFont(None, 35)

def snakeCreator(snakeBody, snakeStomach):
    for x in snakeStomach:
        pygame.draw.rect(dis, green, [x[0], x[1], snakeBody, snakeBody])

def displayScore(score):
    scoreValue = scoreFont.render("Your Score: " + str(score), True, yellow)
    dis.blit(scoreValue, [0, 0])

def message(msg, color):
    mesg = gameFont.render(msg, True, color)
    dis.blit(mesg, [displayWidth / 6, displayHeight / 3])
 
def gameLoop():
    gameOver = False
    gameClass = False
 
    x1 = displayWidth / 2
    y1 = displayHeight / 2
 
    x1_change = 0
    y1_change = 0
 
    snakeStomach = []
    lengthOfStomach = 1
 
    foodx = round(random.randrange(0, displayWidth - snakeBody) / 10.0) * 10.0
    foody = round(random.randrange(0, displayHeight - snakeBody) / 10.0) * 10.0
 
    while not gameOver:
 
        while gameClass == True:
            dis.fill(black)
            message("Press C to Play Again or Q to Quit", red)
            displayScore(lengthOfStomach - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        menu.mainloop(surface)
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snakeBody
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snakeBody
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snakeBody
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snakeBody
                    x1_change = 0
 
        if x1 >= displayWidth or x1 < 0 or y1 >= displayHeight or y1 < 0:
            gameClass = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, white, [foodx, foody, snakeBody, snakeBody])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snakeStomach.append(snake_Head)
        if len(snakeStomach) > lengthOfStomach:
            del snakeStomach[0]
 
        for x in snakeStomach[:-1]:
            if x == snake_Head:
                gameClass = True
 
        snakeCreator(snakeBody, snakeStomach)
        displayScore(lengthOfStomach - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, displayWidth - snakeBody) / 10.0) * 10.0
            foody = round(random.randrange(0, displayHeight - snakeBody) / 10.0) * 10.0
            lengthOfStomach += 1
 
        clock.tick(snakeSpeed)
    pygame.quit()
    quit()
    pass

# CURRENTLY NOT WORKING, FIX
def set_difficulty(value, difficulty):
#    if value == 1:
#    	pass
#    elif value == 2:
#    	displayWidth = 600
#    	displayHeight = 600
#    	snakeSpeed = 25 
#    else:
#    	displayWidth = 800
#    	displayHeight = 800
#    	snakeSpeed = 30
	pass
	

# ADD AI PLAY FEATURE
def start_the_AI():
    pass    

# ADD AI SCORE MENU FEATURE
def scoreMenu():
	pass

menu = pygame_menu.Menu(400, 400, 'Snake Solver',
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name : ', default='Player 1')
menu.add.selector('Difficulty : ', [('Easy', 1), ('Difficult', 2), ('Extreme', 3)], onchange=set_difficulty)
menu.add.button('Play', gameLoop)
menu.add.button('AI Play', start_the_AI)
menu.add.button('High Scores', scoreMenu)
menu.add.button('Quit', pygame_menu.events.EXIT)

# START THE GAME !!!
menu.mainloop(surface)