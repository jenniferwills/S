#levels

#import libraries
import pygame
import constants
import platforms
import monsters
import health_functions

#create general class Level
class Level():
    def __init__(self, player):
        #create lists that can be added to and updated
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.exit_list = pygame.sprite.Group()
        self.health_pack_list = pygame.sprite.Group()
        self.player = player
        #where the player starts
        self.start_pos = 0

    def update(self):
        #update necessary/moving lists
        self.enemy_list.update()
        self.platform_list.update()
        self.health_pack_list.update()

    def draw(self, screen):
        #draw the level
        screen.blit(self.background, (0, 0))
        self.platform_list.draw(screen)
        self.exit_list.draw(screen)
        self.enemy_list.draw(screen)
        self.health_pack_list.draw(screen)

class Level01(Level):
    #create instance of Level, and customize for level 1
    def __init__(self, player):
        Level.__init__(self, player)

        self.start_pos = 120
        
        self.background = pygame.image.load("level01.png")

        #add platforms to the level
        level_platforms = [[platforms.CLOUD, 200, 250],
                           [platforms.CLOUD, 300, 240],
                           [platforms.CLOUD, 400, 220],
                           [platforms.CLOUD, 500, 200 ]]
        for platform in level_platforms:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        #add the level's exit
        level_exit = [[platforms.EXIT_TOP, 510, 158],
                      [platforms.EXIT_BOTTOM, 510, 179]]
        for l_exit in level_exit:
            block = platforms.Exit(l_exit[0])
            block.rect.x = l_exit[1]
            block.rect.y = l_exit[2]
            block.player = self.player
            self.exit_list.add(block)
            
class Level02(Level):
    #create instance of Level, and customize for level 2
    def __init__(self, player):

        Level.__init__(self, player)

        self.start_pos = 120

        self.background = pygame.image.load("level02.png")

        #add platforms
        level_platforms = [[platforms.GRASS_LEFT, 758, 100],
                           [platforms.GRASS_MIDDLE, 779, 100]]

        for platform in level_platforms:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        #add moving platforms
        block = platforms.MovingPlatform(platforms.GRASS_MIDDLE)
        block.rect.x = 300
        block.rect.y = 200
        block.boundary_top = 100
        block.boundary_bottom = 300
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.GRASS_MIDDLE)
        block.rect.x = 321
        block.rect.y = 100
        block.boundary_left = 321
        block.boundary_right = 737
        block.change_x = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #add the exit
        level_exit = [[platforms.EXIT_TOP, 779, 58],
                      [platforms.EXIT_BOTTOM, 779, 79]]
        for l_exit in level_exit:
            block = platforms.Exit(l_exit[0])
            block.rect.x = l_exit[1]
            block.rect.y = l_exit[2]
            block.player = self.player
            self.exit_list.add(block)
        
class Level03(Level):
    #create instance of Level, and customize for level 3
    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("level03.png")

        self.start_pos = 120

        #add patforms
        level_platforms = [[platforms.ICE_LEFT, 200, 200],
                           [platforms.ICE_MIDDLE, 221, 200],
                           [platforms.ICE_MIDDLE, 242, 200],
                           [platforms.ICE_RIGHT, 263, 200],
                           [platforms.ICE_LEFT, 300, 100],
                           [platforms.ICE_MIDDLE, 321, 100],
                           [platforms.ICE_MIDDLE, 342, 100],
                           [platforms.ICE_MIDDLE, 363, 100],
                           [platforms.ICE_RIGHT, 384, 100],
                           [platforms.ICE_LEFT, 400, 150],
                           [platforms.ICE_MIDDLE, 421, 150],
                           [platforms.ICE_MIDDLE, 442, 150],
                           [platforms.ICE_RIGHT, 463, 150],
                           [platforms.ICE_LEFT, 500, 50],
                           [platforms.ICE_MIDDLE, 521, 50],
                           [platforms.ICE_MIDDLE, 542, 50],
                           [platforms.ICE_MIDDLE, 563, 50],
                           [platforms.ICE_RIGHT, 584, 50],
                           [platforms.ICE_LEFT, 700, 150],
                           [platforms.ICE_MIDDLE, 721, 150],
                           [platforms.ICE_MIDDLE, 742, 150],
                           [platforms.ICE_MIDDLE, 763, 150],
                           [platforms.ICE_MIDDLE, 784, 150]]
        for platform in level_platforms:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
    
        #add exit
        level_exit = [[platforms.EXIT_TOP, 779, 108],
                      [platforms.EXIT_BOTTOM, 779, 129]]
        for l_exit in level_exit:
            block = platforms.Exit(l_exit[0])
            block.rect.x = l_exit[1]
            block.rect.y = l_exit[2]
            block.player = self.player
            self.exit_list.add(block)

class Level04(Level):
    #create instance of Level, and customize for level 4
    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("level04.png")

        self.start_pos = 120

        #add platforms
        level_platforms = [[platforms.PURPLE_STONE_LEFT, 200, 200],
                           [platforms.PURPLE_STONE_MIDDLE, 221, 200],
                           [platforms.PURPLE_STONE_MIDDLE, 242, 200],
                           [platforms.PURPLE_STONE_RIGHT, 263, 200],
                           [platforms.PURPLE_STONE_LEFT, 300, 100],
                           [platforms.PURPLE_STONE_MIDDLE, 321, 100],
                           [platforms.PURPLE_STONE_MIDDLE, 342, 100],
                           [platforms.PURPLE_STONE_MIDDLE, 363, 100],
                           [platforms.PURPLE_STONE_RIGHT, 384, 100],
                           [platforms.PURPLE_STONE_LEFT, 400, 150],
                           [platforms.PURPLE_STONE_MIDDLE, 421, 150],
                           [platforms.PURPLE_STONE_MIDDLE, 442, 150],
                           [platforms.PURPLE_STONE_RIGHT, 463, 150],
                           [platforms.PURPLE_STONE_LEFT, 500, 50],
                           [platforms.PURPLE_STONE_MIDDLE, 521, 50],
                           [platforms.PURPLE_STONE_MIDDLE, 542, 50],
                           [platforms.PURPLE_STONE_MIDDLE, 563, 50],
                           [platforms.PURPLE_STONE_RIGHT, 584, 50],
                           [platforms.PURPLE_STONE_LEFT, 700, 150],
                           [platforms.PURPLE_STONE_MIDDLE, 721, 150],
                           [platforms.PURPLE_STONE_MIDDLE, 742, 150],
                           [platforms.PURPLE_STONE_MIDDLE, 763, 150],
                           [platforms.PURPLE_STONE_MIDDLE, 784, 150]]

        for platform in level_platforms:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        #add exit
        level_exit = [[platforms.EXIT_TOP, 779, 108],
                      [platforms.EXIT_BOTTOM, 779, 129]]
        for l_exit in level_exit:
            block = platforms.Exit(l_exit[0])
            block.rect.x = l_exit[1]
            block.rect.y = l_exit[2]
            block.player = self.player
            self.exit_list.add(block)

        #add an enemy to the level
        enemy = monsters.Monster(monsters.BLUE_BLOB)
        enemy.rect.x = 200
        enemy.rect.y = 179
        enemy.boundary_left = 200
        enemy.boundary_right = 263
        enemy.change_x = -1
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        

class Level05(Level):
    #create instance of Level, and customize for level 5
    def __init__(self,player):
        Level.__init__(self, player)

        self.background = pygame.image.load("level05.png")

        self.start_pos = 750

        #add platforms
        level_platforms = [[platforms.MUSH_RED_LEFT, 495, 200],
                           [platforms.MUSH_RED_MIDDLE , 516, 200],
                           [platforms.MUSH_RED_RIGHT , 537, 200],
                    
                           [platforms.MUSH_RED_LEFT, 395, 100],
                           [platforms.MUSH_RED_MIDDLE , 416, 100],
                           [platforms.MUSH_RED_RIGHT , 437, 100],
                           
                           [platforms.MUSH_RED_LEFT, 300, 150],
                           [platforms.MUSH_RED_MIDDLE, 321, 150],
                           [platforms.MUSH_RED_RIGHT,  342, 150],
                           
                           [platforms.MUSH_RED_LEFT, 195, 50],
                           [platforms.MUSH_RED_MIDDLE , 216, 50],
                           [platforms.MUSH_RED_RIGHT , 237, 50],
                           
                           [platforms.MUSH_RED_LEFT, 95, 150],
                           [platforms.MUSH_RED_MIDDLE , 116, 150],
                           [platforms.MUSH_RED_RIGHT , 137, 150]]

        for platform in level_platforms:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


        #add exit
        level_exit = [[platforms.EXIT_TOP, 115, 108],
                      [platforms.EXIT_BOTTOM, 115, 129]]
        for l_exit in level_exit:
            block = platforms.Exit(l_exit[0])
            block.rect.x = l_exit[1]
            block.rect.y = l_exit[2]
            block.player = self.player
            self.exit_list.add(block)


        #add an enemy
        enemy = monsters.Monster(monsters.SPIDER)
        enemy.rect.x = 300
        enemy.rect.y = 130
        enemy.boundary_left = 300
        enemy.boundary_right = 363
        enemy.change_x = -1
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)

        
class Level06(Level):
    #create instance of Level, and customize for level 6
    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("level06.png")

        self.start_pos = 650

        #add enemies to the level
        enemy = monsters.Monster(monsters.BAT)
        enemy.rect.x = 100
        enemy.rect.y = 222
        enemy.boundary_bottom = 300
        enemy.boundary_top = 200
        enemy.change_y = 5
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)

        enemy = monsters.Monster(monsters.BAT)
        enemy.rect.x = 200
        enemy.rect.y = 230
        enemy.boundary_bottom = 300
        enemy.boundary_top = 200
        enemy.change_y = -4
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)

        enemy = monsters.Monster(monsters.BAT)
        enemy.rect.x = 300
        enemy.rect.y = 270
        enemy.boundary_bottom = 300
        enemy.boundary_top = 200
        enemy.change_y = 2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)

        enemy = monsters.Monster(monsters.BAT)
        enemy.rect.x = 400
        enemy.rect.y = 230
        enemy.boundary_bottom = 300
        enemy.boundary_top = 200
        enemy.change_y = -4
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)

        enemy = monsters.Monster(monsters.BAT)
        enemy.rect.x = 500
        enemy.rect.y = 222
        enemy.boundary_bottom = 300
        enemy.boundary_top = 200
        enemy.change_y = 5
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)

        #add exit
        level_exit = [[platforms.EXIT_TOP, 0, 258],
                      [platforms.EXIT_BOTTOM, 0, 279]]
        for l_exit in level_exit:
            block = platforms.Exit(l_exit[0])
            block.rect.x = l_exit[1]
            block.rect.y = l_exit[2]
            block.player = self.player
            self.exit_list.add(block)

        #add health pack
        health_pack = health_functions.Health_Pack()
        health_pack.rect.x = 750
        health_pack.rect.y = 270
        health_pack.level = self
        self.health_pack_list.add(health_pack)


class Level07(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("level07.png")
        self.start_pos = 42

        level_platforms = [[platforms.STONE_LEFT , 21, 100],
                           [platforms.STONE_MIDDLE , 42, 100],
                           [platforms.STONE_MIDDLE , 63, 100],
                           [platforms.STONE_RIGHT , 84, 100],
                           
                           [platforms.STONE_LEFT , 737, 150],
                           [platforms.STONE_MIDDLE , 758, 150],
                           [platforms.STONE_RIGHT , 779, 150]]

        for platform in level_platforms:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        #add moving platforms
        block = platforms.MovingPlatform(platforms.STONE_MIDDLE)
        block.rect.x = 0
        block.rect.y = 121
        block.boundary_top = 100
        block.boundary_bottom = 279
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_MIDDLE)
        block.rect.x = 105
        block.rect.y = 100
        block.boundary_left = 105
        block.boundary_right = 718
        block.change_x = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_MIDDLE)
        block.rect.x = 105
        block.rect.y = 200
        block.boundary_left = 100
        block.boundary_right = 300
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #add enemies to the level
        enemy = monsters.Monster(monsters.BAT)
        enemy.rect.x = 100
        enemy.rect.y = 0
        enemy.boundary_bottom =  95
        enemy.boundary_top = 0
        enemy.change_y = 3
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)

        enemy = monsters.Monster(monsters.BAT)
        enemy.rect.x = 200
        enemy.rect.y = 0
        enemy.boundary_bottom = 95
        enemy.boundary_top = 0
        enemy.change_y = -2
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)

        #add health pack
        health_pack = health_functions.Health_Pack()
        health_pack.rect.x = 42
        health_pack.rect.y = 79
        health_pack.level = self
        self.health_pack_list.add(health_pack)

        
        #add exit
        level_exit = [[platforms.EXIT_TOP, 779, 108],
                      [platforms.EXIT_BOTTOM, 779, 129]]
        for l_exit in level_exit:
            block = platforms.Exit(l_exit[0])
            block.rect.x = l_exit[1]
            block.rect.y = l_exit[2]
            block.player = self.player
            self.exit_list.add(block)

