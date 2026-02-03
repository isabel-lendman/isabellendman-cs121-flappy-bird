'''
grapics_sound.py

Authors:
    Liam McCullar

Description:
    This file will contain all the pygame graphic imports and music :D
Dependencies:

graphics_sound

'''
import pygame 
import random
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

BG_COLOR = (0, 255, 255)

import pygame, sys
from graphics_sound import *
from pygame import mixer 


###music
# Starting the mixer 



def menu_screen(window):
    window = pygame.display.set_mode((600, 400))
    run = True

    # Main screen Music
    mixer.init() 
    mixer.music.load("menuscreen.mp3")
    mixer.music.play() 

    # Game Logo
    logo = pygame.image.load('logo.png')
    default_img_size = (200, 50)
    new_logo = pygame.transform.scale(logo, default_img_size)

    # Main Menu Graphics
    thumbs_up = pygame.image.load('dude.png')
    new_thumb = pygame.transform.scale(thumbs_up, default_img_size)
    fun = pygame.image.load('fun.png')
    new_fun = pygame.transform.scale(fun, default_img_size)

    # Main Menu Game Loop
    while run:
        window.blit(imp, (0, 0))
        window.blit(new_logo, (200, 30))
        window.blit(new_thumb, (25, 100))
        window.blit(new_fun, (400, 180))

    
        Menu_Mouse_Pos = pygame.mouse.get_pos()

        # Main Menu Buttons
        PLAY_BUTTON = Button(image=pygame.image.load("neon_button.png"),x_pos=300, y_pos=200, text_input="PLAY", font="arailblack", base_color="#884DFF", hovering_color="White", scale=0.5)
        

        for button in [PLAY_BUTTON]:
            button.changeColor(Menu_Mouse_Pos)
            button.update(window)



        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(Menu_Mouse_Pos):
                    game_screen(window)
                
                    
        
        pygame.display.flip()


# Window variable for draw_text function
window = pygame.display.set_mode((600,400))

# Font for Score
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))
    

# Game Screen Function
def game_screen(window):


    bird_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()
    flappy = Bird(100, int(WINDOW_HEIGHT /2))
    bird_group.add(flappy)
    game_over = False
    window = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Game Screen")
    bg = pygame.image.load('hell_2.webp')
    floor = pygame.image.load('ground.png')
    game_over_img = pygame.image.load('restart.png')


    # defining font
    font = pygame.font.SysFont('Bauhaus 93', 60)
    white = (255, 255, 255)

    # game variables
    clock = pygame.time.Clock()
    fps = 60

    pipe_frequency = 1500
    last_pipe = pygame.time.get_ticks() - pipe_frequency
    ground_scroll = 0

    ground_scroll = 0
    scroll_speed = 4

    flying = False
    game_over = False
    pygame.display.flip()
    run = True
    score = 0 
    pass_pipe = False

    # Game over Button

    game_over_button = Game_Over(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 100, game_over_img)

#game screen music
# Loading the song 
    mixer.music.load("FlappyMusic.mp3") 
    mixer.music.play() 


    while run:
        clock.tick(fps)
        window.blit(bg, (0, 0))

        bird_group.draw(window)
        bird_group.update()
        pipe_group.draw(window)
        
        # Draw ground
        window.blit(floor, (ground_scroll, 600))

        # checking score

        if len(pipe_group) > 0:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
                and pass_pipe == False:
                pass_pipe = True
            if pass_pipe == True:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    pass_pipe = False
        draw_text(str(score), font, white, int(WINDOW_WIDTH / 2), 20)

        # Check if bird hit ground

        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
            game_over = True
            
        

        if flappy.rect.bottom >= 600:
            game_over = True
            flying = False
            

        if game_over == False:  

            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > pipe_frequency:
                pipe_height = random.randint(-100, 100)
                btm_pipe = Pipe(WINDOW_WIDTH, int(WINDOW_HEIGHT /2) + pipe_height, -1)
                top_pipe = Pipe(WINDOW_WIDTH, int(WINDOW_HEIGHT /2) + pipe_height, 1)
                pipe_group.add(top_pipe)
                pipe_group.add(btm_pipe)
                last_pipe = time_now


            ground_scroll -= scroll_speed
            if abs(ground_scroll) > 35:
                ground_scroll = 0


            pipe_group.update()
        

        # Check for game over

        if game_over == True:
            if game_over_button.draw() == True:
                return game_screen(window)
        
        # Event Handler

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
                flappy.flying = True

        pygame.display.update()


    pygame.display.flip()


