'''
grapics_sound.py

Authors:
    Liam McCullar

Description:
    This file will contain all the pygame graphic imports and music :D
Dependencies:

global variables

'''

import sys
import pygame
import random
from pygame import mixer
#Local dependencies 
from global_variables import *


pygame.init()
imp = pygame.image.load("background_game_6.jpg")
maint_font = pygame.font.SysFont("arailblack", 25)

window = pygame.display.set_mode((600, 400))



# Button Class
class Button():
    def __init__(self, image, font, base_color, hovering_color, x_pos, y_pos, text_input, scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = maint_font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = maint_font.render(self.text_input, True, self.hovering_color)
        else: 
            self.text = maint_font.render(self.text_input, True, self.base_color)



class Game_Over():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        window.blit(self.image, (self.rect.x, self.rect.y))
        return action



class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pipe.png')
        self.rect = self.image.get_rect()
        # position 1 is from the top, -1 is from the bottom
        pipe_gap = 200
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]
    def update(self):
        pipe_frequency = 1500
        last_pipe = pygame.time.get_ticks()
        ground_scroll = 0
        scroll_speed = 4
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()
    def delete_me(self):
        self.x = 300000

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.click = False

    def update(self):
        # gravity
        self.vel += 0.5
        if self.vel > 8:
            self.vel = 8
        if self.rect.bottom < 600:
           self.rect.y += int(self.vel)

        #jump
        if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
            self.click = True
            self.vel = -10
        if pygame.mouse.get_pressed()[0] == 1:
            self.click = False


        # handle animation
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

        # Rotate Byrd

        self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)



# bird_group = pygame.sprite.Group()
# pipe_group = pygame.sprite.Group()
# flappy = Bird(100, int(WINDOW_HEIGHT /2))
# bird_group.add(flappy)


