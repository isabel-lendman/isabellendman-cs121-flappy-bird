'''
elements.py

Authors:
    Isabel 
    Elliot
    Liam
    Cameron

Description:
    This file will contain all the elements needed to create a game similiar to flappy bird

Dependemcies:
    -sys
    -pygame
'''
import sys
import pygame

# Local Dependencies
from Screens import *
from global_variables import *

pygame.init()
window = pygame.display.set_mode((600,400))
# The Loop
# This keeps track of which screen we are looking at.
current_screen = "menu"
while True:
    if current_screen == "menu":
        menu_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


Flappy_image = pygame.image.load("download")
