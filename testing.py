import pygame
from math_functions import compareSquares
from data_structures import Point

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
    sq1 = Point(100, 100)
    sq1_width = 40
    pygame.draw.rect(surface, BEIGE, [sq1.x, sq1.y, sq1_width, sq1_width])
    # SQUARE TWO 
    sq2 = Point(140, 100)
    sq2_width = 40
    pygame.draw.rect(surface, ORANGE, [sq2.x, sq2.y, sq2_width, sq2_width])
    # Comparison SQ1 and SQ2
    heading1 = font.render("Testing Collision when exactly adjacent. Expectation = Collision", True, TEXT)
    surface.blit(heading1, (100, 70))
    if compareSquares(sq1, sq2, sq1_width, sq2_width):
        text = font.render("[Collision] x1 = {}, x2 = {}".format(sq1.x, sq2.x), True, TEXT)
    else:
        text = font.render("[No Collision] x1 = {}, x2 = {}".format(sq1.x, sq2.x), True, TEXT)
    surface.blit(text, (300, 110))

    # TESTING CASE II
    # SQUARE THREE
    sq3 = Point(100, 200)
    sq3_width = 40
    pygame.draw.rect(surface, BEIGE, [sq3.x, sq3.y, sq3_width, sq3_width])
    # SQUARE FOUR
    sq4 = Point(139, 200)
    sq4_width = 40
    pygame.draw.rect(surface, ORANGE, [sq4.x, sq4.y, sq4_width, sq4_width])
    # Comparison SQ3 and SQ4
    heading1 = font.render("Testing Collision when one pixel inside. Expectation = Collision", True, TEXT)
    surface.blit(heading1, (100, 170))
    if compareSquares(sq3, sq4, sq3_width, sq4_width):
        text = font.render("[Collision] x1 = {}, x2 = {}".format(sq3.x, sq4.x), True, TEXT)
    else:
        text = font.render("[No Collision] x1 = {}, x2 = {}".format(sq3.x, sq4.x), True, TEXT)
    surface.blit(text, (300, 210))

    # TESTING CASE III
    # SQUARE FIVE
    sq5 = Point(100, 300)
    sq5_width = 40
    pygame.draw.rect(surface, BEIGE, [sq5.x, sq5.y, sq5_width, sq5_width])
    # SQUARE SIX
    sq6 = Point(141, 300)
    sq6_width = 40
    pygame.draw.rect(surface, ORANGE, [sq6.x, sq6.y, sq6_width, sq6_width])
    # Comparison SQ5 and SQ6
    heading1 = font.render("Testing Collision when one pixel away. Expectation = No Collision", True, TEXT)
    surface.blit(heading1, (100, 270))
    if compareSquares(sq5, sq6, sq5_width, sq6_width):
        text = font.render("[Collision] x1 = {}, x2 = {}".format(sq5.x, sq6.x), True, TEXT)
    else:
        text = font.render("[No Collision] x1 = {}, x2 = {}".format(sq5.x, sq6.x), True, TEXT)
    surface.blit(text, (300, 310))

    # TESTING CORNERS
    heading1 = font.render("Testing Collision For Corners. Expectation = Collision", True, TEXT)
    surface.blit(heading1, (100, 370))

    # TESTING CASE IV TOP RIGHT
    # SQUARE SEVEN
    sq7 = Point(100, 440)
    sq7_width = 40
    pygame.draw.rect(surface, BEIGE, [sq7.x, sq7.y, sq7_width, sq7_width])
    # SQUARE EIGHT

    sq8 = Point(139, 401)
    sq8_width = 40
    pygame.draw.rect(surface, ORANGE, [sq8.x, sq8.y, sq8_width, sq8_width])
    # Comparison SQ7 and SQ8
    
    if compareSquares(sq7, sq8, sq7_width, sq8_width):
        text = font.render("[Collision] x1 = {}, x2 = {}".format(sq7.x, sq8.x), True, TEXT)
    else:
        text = font.render("[No Collision] x1 = {}, x2 = {}".format(sq7.x, sq8.x), True, TEXT)
    surface.blit(text, (300, 420))

    # TESTING CASE V BOTTOM
    # SQUARE NINE
    sq9 = Point(140, 539)
    sq9_width = 40
    pygame.draw.rect(surface, BEIGE, [sq9.x, sq9.y, sq9_width, sq9_width])
    # SQUARE TEN
    sq10 = Point(101, 500)
    sq10_width = 40
    pygame.draw.rect(surface, ORANGE, [sq10.x, sq10.y, sq10_width, sq10_width])
    # Comparison SQ9 and SQ10
    
    if compareSquares(sq9, sq10, sq9_width, sq10_width):
        text = font.render("[Collision] x1 = {}, x2 = {}".format(sq9.x, sq10.x), True, TEXT)
    else:
        text = font.render("[No Collision] x1 = {}, x2 = {}".format(sq9.x, sq10.x), True, TEXT)
    surface.blit(text, (300, 520))

    # Testing Case VI Square Exactly Within Square
    heading1 = font.render("Testing Square Within Square. Expectation = Collision", True, TEXT)
    surface.blit(heading1, (100, 650))
    # SQUARE TEN
    sq11 = Point(100, 680)
    sq11_width = 40
    pygame.draw.rect(surface, BEIGE, [sq11.x, sq11.y, sq11_width, sq11_width])
    # SQUARE ELEVEN
    sq12 = Point(110, 710)
    sq12_width = 20
    pygame.draw.rect(surface, ORANGE, [sq12.x, sq12.y, sq12_width, sq12_width])
    # Comparison sq11 and sq12
    
    if compareSquares(sq11, sq12, sq11_width, sq12_width):
        text = font.render("[Collision] x1 = {}, x2 = {}".format(sq11.x, sq12.x), True, TEXT)
    else:
        text = font.render("[No Collision] x1 = {}, x2 = {}".format(sq11.x, sq12.x), True, TEXT)
    surface.blit(text, (300, 720))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
    
    pygame.display.update()
    clock.tick(GAME_SPEED)

pygame.quit()