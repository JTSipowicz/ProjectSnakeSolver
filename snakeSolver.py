import pygame
import time
import random
 
pygame.init()
 
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
 
 
def displayScore(score):
    value = scoreFont.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def snakeCreator(snakeBody, snakeStomach):
    for x in snakeStomach:
        pygame.draw.rect(dis, green, [x[0], x[1], snakeBody, snakeBody])
 
 
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
            message("You Lost! Press C-Play Again or Q-Quit", red)
            displayScore(lengthOfStomach - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClass = False
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
 
 
gameLoop()