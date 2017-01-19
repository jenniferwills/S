#Sprite Sheet

import pygame
import constants

class SpriteSheet(object):
    def __init__(self, file_name):

        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        #take a section of the spritesheet
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        #remove the background
        image.set_colorkey(constants.SPRITE_BACK)
        # Return the image
        return image
