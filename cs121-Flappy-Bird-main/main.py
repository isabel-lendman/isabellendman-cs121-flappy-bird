import sys
import pygame



#Local dependencies 
from Screens import *
from global_variables import *

pygame.init()
window = pygame.display.set_mode((600, 700))

# the loop
# keeps track of which screen we are on
current_screen = "menu"
while True: 
    pygame.display.flip()
    if current_screen == "menu" :
            current_screen = menu_screen(window)
            if current_screen == "game" :
                  game_screen()

    for event in pygame.event.get() :
          if event.type == pygame.QUIT :
                sys.exit()
sys.exit()
