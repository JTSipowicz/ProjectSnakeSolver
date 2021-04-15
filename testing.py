import pygame
from math_functions import compareSquares

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BLACK = (0, 0, 0)
BEIGE = '#f7f3e9'
ORANGE = '#e2703a'
TEXT = '#a3d2ca'

GAME_SPEED = 10
isRunning= True

surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Testing")
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

while isRunning:
    surface.fill(BLACK)
    # TESTING CASE I
    # SQUARE ONE
    sq1_x = 100
    sq1_y = 100
    sq1_width = 40
    pygame.draw.rect(surface, BEIGE, [sq1_x, sq1_y, sq1_width, sq1_width])
    # SQUARE TWO 
    sq2_x = 140
    sq2_y = 100
    sq2_width = 40
    pygame.draw.rect(surface, ORANGE, [sq2_x, sq2_y, sq2_width, sq2_width])
    # Comparison SQ1 and SQ2
    heading1 = font.render("Testing Collision when exactly adjacent. Expectation = No Collision", True, TEXT)
    surface.blit(heading1, (100, 70))
    if compareSquares(sq1_x, sq2_x, sq1_y, sq2_y, sq1_width, sq2_width):
        text = font.render("[Collision] x1 = {}, x2 = {}".format(sq1_x, sq2_x), True, TEXT)
    else:
        text = font.render("[No Collision] x1 = {}, x2 = {}".format(sq1_x, sq2_x), True, TEXT)
    surface.blit(text, (300, 110))

    # TESTING CASE II
    # SQUARE THREE
    sq3_x = 100
    sq3_y = 200
    sq3_width = 40
    pygame.draw.rect(surface, BEIGE, [sq3_x, sq3_y, sq3_width, sq3_width])
    # SQUARE FOUR
    sq4_x = 139
    sq4_y = 200
    sq4_width = 40
    pygame.draw.rect(surface, ORANGE, [sq4_x, sq4_y, sq4_width, sq4_width])
    # Comparison SQ3 and SQ4
    heading1 = font.render("Testing Collision when one pixel inside. Expectation = Collision", True, TEXT)
    surface.blit(heading1, (100, 170))
    if compareSquares(sq3_x, sq4_x, sq3_y, sq4_y, sq3_width, sq4_width):
        text = font.render("[Collision] x1 = {}, x2 = {}".format(sq3_x, sq4_x), True, TEXT)
    else:
        text = font.render("[No Collision] x1 = {}, x2 = {}".format(sq3_x, sq4_x), True, TEXT)
    surface.blit(text, (300, 210))

    # TESTING CASE III
    # SQUARE FIVE
    sq5_x = 100
    sq5_y = 300
    sq5_width = 40
    pygame.draw.rect(surface, BEIGE, [sq5_x, sq5_y, sq5_width, sq5_width])
    # SQUARE SIX
    sq6_x = 141
    sq6_y = 300
    sq6_width = 40
    pygame.draw.rect(surface, ORANGE, [sq6_x, sq6_y, sq6_width, sq6_width])
    # Comparison SQ5 and SQ6
    heading1 = font.render("Testing Collision when one pixel away. Expectation = No Collision", True, TEXT)
    surface.blit(heading1, (100, 270))
    if compareSquares(sq5_x, sq6_x, sq5_y, sq6_y, sq5_width, sq6_width):
        text = font.render("[Collision] x1 = {}, x2 = {}".format(sq5_x, sq6_x), True, TEXT)
    else:
        text = font.render("[No Collision] x1 = {}, x2 = {}".format(sq5_x, sq6_x), True, TEXT)
    surface.blit(text, (300, 310))

    # TESTING CORNERS
    heading1 = font.render("Testing Collision For Corners. Expectation = Collision", True, TEXT)
    surface.blit(heading1, (100, 370))

    # TESTING CASE IV TOP RIGHT
    # SQUARE SEVEN
    sq7_x = 100
    sq7_y = 440
    sq7_width = 40
    pygame.draw.rect(surface, BEIGE, [sq7_x, sq7_y, sq7_width, sq7_width])
    # SQUARE EIGHT
    sq8_x = 139
    sq8_y = 401
    sq8_width = 40
    pygame.draw.rect(surface, ORANGE, [sq8_x, sq8_y, sq8_width, sq8_width])
    # Comparison SQ7 and SQ8
    
    if compareSquares(sq7_x, sq8_x, sq7_y, sq8_y, sq7_width, sq8_width):
        text = font.render("[Collision] x1 = {}, x2 = {}".format(sq7_x, sq8_x), True, TEXT)
    else:
        text = font.render("[No Collision] x1 = {}, x2 = {}".format(sq7_x, sq8_x), True, TEXT)
    surface.blit(text, (300, 420))

    # TESTING CASE V BOTTOM
    # SQUARE NINE
    sq9_x = 140
    sq9_y = 539
    sq9_width = 40
    pygame.draw.rect(surface, BEIGE, [sq9_x, sq9_y, sq9_width, sq9_width])
    # SQUARE TEN
    sq10_x = 101
    sq10_y = 500
    sq10_width = 40
    pygame.draw.rect(surface, ORANGE, [sq10_x, sq10_y, sq10_width, sq10_width])
    # Comparison SQ9 and SQ10
    
    if compareSquares(sq9_x, sq10_x, sq9_y, sq10_y, sq9_width, sq10_width):
        text = font.render("[Collision] x1 = {}, x2 = {}".format(sq9_x, sq10_x), True, TEXT)
    else:
        text = font.render("[No Collision] x1 = {}, x2 = {}".format(sq9_x, sq10_x), True, TEXT)
    surface.blit(text, (300, 520))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
    
    pygame.display.update()
    clock.tick(GAME_SPEED)

pygame.quit()