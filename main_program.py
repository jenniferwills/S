

#import important libraries
import pygame
import constants
import levels
import time
from player import Player

def main():
    #main program

    pygame.init()

    #setting up the pygame display
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Platformer")

    #creating instance of class Player to be the user's player
    player = Player()

    #create instances of the levels and add them to the level_list
    level_list = []
    level_list.append(levels.Level01(player))
    level_list.append(levels.Level02(player))
    level_list.append(levels.Level03(player))
    level_list.append(levels.Level04(player))
    level_list.append(levels.Level05(player))
    level_list.append(levels.Level06(player))
    level_list.append(levels.Level07(player))


    #start the game with level 1
    current_level_num = 0
    current_level = level_list[current_level_num]
    
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    #start player on the ground and at an x position specific to the level
    
    player.rect.x = current_level.start_pos
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

   
    
    done = False

    clock = pygame.time.Clock()
    
    while not done:
        #move the player when keys are pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                 
            #stop the player as keys are released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        #update level and player
        active_sprite_list.update()
        current_level.update()       
 
        # If the player gets to the exit of the level, go to the next level
        
        exit_hit_list = pygame.sprite.spritecollide(player, player.level.exit_list, False)
        if len(exit_hit_list)>=1:
            if current_level_num+1 < len(level_list):    
                current_level_num +=1
                current_level = level_list[current_level_num]
                player.level = current_level
                player.rect.x = player.level.start_pos
                player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
            else:
                done =True
   
        #draw level, player and health
        current_level.draw(screen)
        active_sprite_list.draw(screen)        
        for i in range(len(player.health_list)):
            screen.blit(player.health_list[i], [i*21, 0])       
        if player.health == 0:
            #game over when player runs out of health
            done = True
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    #play sound for game over
    game_over = pygame.mixer.music.load("game_over.ogg")
    constants.pygame.mixer.music.play()
    #pause so that the sound completely plays before pygame ends
    time.sleep(3)
    pygame.quit()

    
if __name__ == "__main__":
    main()




