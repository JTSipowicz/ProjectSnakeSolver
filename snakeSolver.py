import pygame
import time
import random
pygame.init()

blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
green = (0,255,0)
black = (0, 0, 0)

displayWidth = 500
displayHeight  = 500
dis = pygame.display.set_mode((displayWidth, displayWidth))
pygame.display.set_caption('JSIPs Snake')

clock = pygame.time.Clock()
snakeBody = 10
snakeSpeed = 25

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 25)

def ourSnake(snakeBody, snakeList):
	for x in snakeList:
		pygame.draw.rect(dis, green, [x[0], x[1], snakeBody, snakeBody])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [displayWidth/6, displayHeight/3])

def displayedScore(currentScore):
	viewableScore = score_font.render("Current Score: " + str(currentScore), True, green)
	dis.blit(viewableScore, [0,0])

def gameLoop():
	gameOver = False
	gameClose = False

	x1 = displayWidth/2
	y1 = displayHeight/2
	x1_change = 0       
	y1_change = 0
	snakeList = []
	snakeLength = 2

	foodx = round(random.randrange(0, displayWidth - snakeBody) / 10.0) * 10.0
	foody = round(random.randrange(0, displayHeight - snakeBody) / 10.0) * 10.0
	
	while not gameOver:
		while gameClose == True:
			dis.fill(white)
			message ("Game Over! Press Q to quit or C to try again...", red)
			displayedScore(snakeLength - 1)

			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameOver = True
						gameClose = False
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
			gameClose = True
		x1 += x1_change
		y1 += y1_change
		dis.fill(black)
		pygame.draw.rect(dis, blue, [foodx, foody, snakeBody, snakeBody])
		snakeHead = []
		snakeHead.append(x1)
		snakeHead.append(y1)
		snakeHead.append(snakeHead)
		if len(snakeList) > snakeLength:
			del snakeList[0]

		for x in snakeList[:-1]:
			if x == snakeHead:
				gameClose = True

		ourSnake(snakeBody, snakeList)
		displayedScore(snakeLength - 1)

		pygame.display.update()

		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0, displayWidth - snakeBody) / 10.0) * 10.0
			foody = round(random.randrange(0, displayWidth - snakeBody) / 10.0) * 10.0
			snakeLength += 1

		clock.tick(snakeSpeed)

	pygame.quit()
	quit()

# Run the game.
gameLoop()