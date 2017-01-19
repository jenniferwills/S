#Constants Library

import pygame

# Colors
BLACK       = (   0,   0,   0) 
WHITE       = ( 255, 255, 255) 
BLUE        = (   0,   0, 255)
SPRITE_BACK = (  94, 129, 162)

# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 300

#initialize and load hit sound
pygame.mixer.init()
hit_sounds = pygame.mixer.music.load("hurt.ogg")


