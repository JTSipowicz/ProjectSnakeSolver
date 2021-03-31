import pygame
import time
import random
pygame.init()

blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
green = (0,255,0)
black = (0, 0, 0)

dis_width = 500
dis_height  = 500
dis = pygame.display.set_mode((dis_width, dis_width))
pygame.display.set_caption('JSIPs Snake')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 25

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 25)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

def displayedScore(currentScore):
	viewableScore = score_font.render("Current Score: " + str(currentScore), True, green)
	dis.blit(viewableScore, [0,0])

def ourSnake(snake_block, snakeList):
	for x in snakeList:
		pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def gameLoop():
	gameOver = False
	gameClose = False

	x1 = dis_width/2
	y1 = dis_height/2
	x1_change = 0       
	y1_change = 0
	snakeList = []
	Length_of_snake = 1

	foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
	foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
	
	while not gameOver:
		while gameClose == True:
			dis.fill(white)
			message ("Game Over! Press Q to quit or C to try again...", red)
			displayedScore(Length_of_snake - 1)
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
					x1_change = -snake_block
					y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = snake_block
					y1_change = 0
				elif event.key == pygame.K_UP:
					y1_change = -snake_block
					x1_change = 0
				elif event.key == pygame.K_DOWN:
					y1_change = snake_block
					x1_change = 0
		if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
			gameClose = True
		x1 += x1_change
		y1 += y1_change
		pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
		snakeHead = []
		snakeHead.append(x1)
		snakeHead.append(y1)
		snakeHead.append(snakeHead)
		if len(snakeList) > Length_of_snake:
			del snakeList[0]

		for x in snakeList[:-1]:
			if x == snakeHead:
				gameClose = True

		ourSnake(snake_block, snakeList)
		displayedScore(Length_of_snake - 1)

		pygame.display.update()

		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
			foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
			Length_of_snake += 1

		clock.tick(snake_speed)

	pygame.quit()
	quit()

# Run the game.
gameLoop()