#monsters

#import libraries
import pygame
import constants
import levels
import player
from spritesheet_functions import SpriteSheet
import platforms


#where in the sprite sheet png are these enemies and their animations
BLUE_BLOB  = ([439, 209, 21, 21],
              [462, 209, 21, 21],
              [485, 209, 21, 21])
BAT        = ([462, 324, 21, 21],
              [485, 324, 21, 21],
              [508, 324, 21, 21])
SPIDER     = ([462, 347, 21, 21],
              [485, 347, 21, 21],
              [508, 347, 21, 21])

class Monster(pygame.sprite.Sprite):
    #create the general monster sprite
    def __init__(self, monster_type):
        super().__init__()

        
        #allow the enemy to move
        self.change_x = 0
        self.change_y = 0
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.direction = "R"

        
        #create list of the enemy's animation
        self.walking_frames_l = []
        self.walking_frames_r = []
        sprite_sheet = SpriteSheet("spritesheet.png")
        self.frame_change = 0

        #images for enemy moving right
        image = sprite_sheet.get_image(monster_type[0][0],
                                       monster_type[0][1],
                                       monster_type[0][2],
                                       monster_type[0][3])
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(monster_type[1][0],
                                       monster_type[1][1],
                                       monster_type[1][2],
                                       monster_type[1][3])
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(monster_type[2][0],
                                       monster_type[2][1],
                                       monster_type[2][2],
                                       monster_type[2][3])
        self.walking_frames_r.append(image)
        
        #images for enemy moving left
        image = sprite_sheet.get_image(monster_type[0][0],
                                       monster_type[0][1],
                                       monster_type[0][2],
                                       monster_type[0][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(monster_type[1][0],
                                       monster_type[1][1],
                                       monster_type[1][2],
                                       monster_type[1][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(monster_type[2][0],
                                       monster_type[2][1],
                                       monster_type[2][2],
                                       monster_type[2][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
    
        self.frame = 0
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
        
    def update(self):

        self.rect.x += self.change_x
        #change the frame as the enemy moves
        if self.change_x != 0 or self.change_y != 0:
            self.frame_change+=1
        if self.direction == "R" and self.frame_change ==10:
            self.frame_change = 0
            self.frame +=1
            if self.frame>len(self.walking_frames_r)-1:
                self.frame = 0
            self.image = self.walking_frames_r[self.frame]
        elif self.direction == "L" and self.frame_change == 10:
            self.frame_change = 0
            self.frame +=1
            if self.frame>len(self.walking_frames_l)-1:
                self.frame = 0
            self.image = self.walking_frames_l[self.frame]


        self.rect.y += self.change_y

        #allow the enemy to use platforms as well as the player
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
             # Reset enemy position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            self.change_y = 0

        #the enemy will only move within certain boundaries 
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        if self.rect.x < self.boundary_left or self.rect.x > self.boundary_right:
            self.change_x *= -1
