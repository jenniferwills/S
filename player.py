#player

import pygame
import constants
from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet
import health_functions

class Player(pygame.sprite.Sprite):
    #create the general class Player
    def __init__(self):
        super().__init__()
        self.change_x = 0
        self.change_y = 0

        self.level = None

        #give the player health
        self.health = 10
        #allow the health to be displayed on the screen
        self.health_images = []
        sprite_sheet = SpriteSheet("spritesheet.png")
        image = sprite_sheet.get_image(347, 278, 21, 21)
        self.health_images.append(image)
        image = sprite_sheet.get_image(324, 278, 21, 21)
        self.health_images.append(image)
        image = sprite_sheet.get_image(301, 278, 21, 21)
        self.health_images.append(image)
        self.health_list = [self.health_images[2],
                            self.health_images[2],
                            self.health_images[2],
                            self.health_images[2],
                            self.health_images[2]]


        #give the player animations
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.direction = "R"    
        sprite_sheet = SpriteSheet("spritesheet.png")

        #images for player moving right
        image = sprite_sheet.get_image(439, 2, 21, 21)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(462, 2, 21, 21)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(646, 2, 21, 21)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(669, 2, 21, 21)
        self.walking_frames_r.append(image)
        #images for player moving left
        image = sprite_sheet.get_image(439, 2, 21, 21)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(462, 2, 21, 21)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(646, 2, 21, 21)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(669, 2, 21, 21)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        self.frame_speed = 0
        self.frame = 0
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()

    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x
        #change frames only when the player is moving
        if self.change_x !=0: 
            self.frame_speed+=1
        if self.direction == "R" and self.frame_speed == 5:
            self.frame_speed = 0
            self.frame +=1
            if self.frame>len(self.walking_frames_r)-1:
                self.frame =0
            self.image = self.walking_frames_r[self.frame]
            
        elif self.direction == "L" and self.frame_speed == 5:
            self.frame_speed = 0
            self.frame +=1
            if self.frame>len(self.walking_frames_l)-1:
                self.frame =0
            self.image = self.walking_frames_l[self.frame]

        self.rect.y += self.change_y

        #stay on the platforms 
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x >0 and self.rect.right <=block.rect.left and self.rect.bottom >= block.rect.top:
                self.rect.right = block.rect.x 
            elif self.change_x<0 and self.rect.left>=block.rect.right and self.rect.bottom >= block.rect.top:
                self.rect.left = block.rect.right
            if self.change_y > 0 and self.rect.left <= block.rect.right and self.rect.right>=block.rect.left:
                self.rect.bottom = block.rect.top
                self.change_y = 0
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
                self.change_y = 0

            #if the platform moves, keep the player from falling off of it
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
        #do not let the player walk offscreen        
        if self.rect.x >=779:
            self.rect.x = 779
        elif self.rect.x <= 0:
            self.rect.x = 0

        self.health_check()
        
    def health_check(self):
        #add health if there is a health pack
        health_hit_list = pygame.sprite.spritecollide(self, self.level.health_pack_list, True)
        for pack in health_hit_list:
            self.health+=1
            if self.health>10:
                self.health = 10
        #lose health if it is an enemy
        enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        if len(enemy_hit_list)>0:
            self.health-=1
            #play hit sound when the player loses health
            constants.pygame.mixer.music.play()
            if self.direction == "R":
                self.rect.x -=10
            else:
                self.rect.x +=10
        #display hearts to show the health
        if self.health==9:
            self.health_list[4] = self.health_images[1]
        if self.health==8:
            self.health_list[4] = self.health_images[0]
        if self.health==7:
            self.health_list[3] = self.health_images[1]
        if self.health==6:
            self.health_list[3] = self.health_images[0]
        if self.health==5:
            self.health_list[2] = self.health_images[1]
        if self.health==4:
            self.health_list[2] = self.health_images[0]
        if self.health==3:
            self.health_list[1] = self.health_images[1]
        if self.health==2:
            self.health_list[1] = self.health_images[0]
        if self.health==1:
            self.health_list[0] = self.health_images[1]
        if self.health==0:
            self.health_list[0] = self.health_images[0]
                 
    def calc_grav(self):
        #the player can jump and fall off platforms
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .25

         #do not fall through the ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height


    def jump(self):

        #only jump when there is something underneath the player.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -7
 
    # Player-controlled movement:
    def go_left(self):
        self.change_x = -3
        self.direction = "L"
 
    def go_right(self):
        self.change_x = 3
        self.direction = "R"
 
    def stop(self):
        self.change_x = 0














































  
