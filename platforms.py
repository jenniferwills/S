#Platforms

import pygame
import constants

from spritesheet_functions import SpriteSheet



'''Define the platform types
name = (x, y, width, height)
'''

#clouds
CLOUD                 = (416, 140, 38, 21)

GRASS_LEFT            = (117,  94, 21, 21)
GRASS_MIDDLE          = ( 71,  94, 21, 21)
GRASS_RIGHT           = (117, 117, 21, 21)

ICE_LEFT              = (117, 370, 21, 21)
ICE_MIDDLE            = ( 71, 370, 21, 21)
ICE_RIGHT             = (117, 393, 21, 21)
ICE_CENTRE             = ( 48, 393, 21, 21)

PURPLE_STONE_LEFT     = (117, 140, 21, 21)
PURPLE_STONE_MIDDLE   = ( 71, 140, 21, 21)
PURPLE_STONE_RIGHT    = (117, 163, 21, 21)

STONE_LEFT            = (117, 232, 21, 21)
STONE_MIDDLE          = ( 71, 232, 21, 21)
STONE_RIGHT           = (117, 255, 21, 21)

#Mushrooms
MUSH_RED_LEFT         = ( 25, 278, 21, 21)
MUSH_RED_MIDDLE       = ( 48, 278, 21, 21)
MUSH_RED_RIGHT        = ( 95, 278, 21, 21)

#EXITING LEVELS
EXIT_TOP              = (232, 531, 21, 21)
EXIT_BOTTOM           = (232, 554, 21, 21)






class Exit(pygame.sprite.Sprite):
    #general class exit so that the player can quit and move on to the next level
    def __init__(self, sprite_sheet_data):
        super().__init__()
        sprite_sheet = SpriteSheet("spritesheet.png")
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
                                            
        self.image.set_colorkey(constants.SPRITE_BACK)
        self.rect = self.image.get_rect()

class Platform(pygame.sprite.Sprite):
    #platform for the user to jump on

    def __init__(self, sprite_sheet_data):
        super().__init__()

        #get the specific blocks from the sprite sheet
        sprite_sheet = SpriteSheet("spritesheet.png")
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.image.set_colorkey(constants.SPRITE_BACK)
        self.rect = self.image.get_rect()

class MovingPlatform(Platform):
    #general class for a moving platform
    def __init__(self, sprite_sheet_data):
 
        super().__init__(sprite_sheet_data)
 
        self.change_x = 0
        self.change_y = 0
 
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
 
        self.level = None
        self.player = None

    def update(self):
        #move left/right and up/down
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        #check to see if platform should reverse direction
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        if self.rect.x  < self.boundary_left or self.rect.x  > self.boundary_right:
            self.change_x *= -1




































        
