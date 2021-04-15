import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((800, 400))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

def start_the_AI():
    # Do the job here !
    pass    

menu = pygame_menu.Menu(300, 400, 'Snake Solver',
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='James Sip')
menu.add.selector('Difficulty :', [('Small', 1), ('Medium', 2), ('Large', 3)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('AI Play', start_the_AI)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
