#health

#import libraries
import pygame
import constants
from spritesheet_functions import SpriteSheet


class Health_Pack(pygame.sprite.Sprite):
    #allow the player to regain health via health packs
    def __init__(self):
        super().__init__()
        
        sprite_sheet = SpriteSheet("spritesheet.png")
        self.image = sprite_sheet.get_image(602, 669, 21, 21)
        self.image.set_colorkey(constants.SPRITE_BACK)

        self.rect = self.image.get_rect()

