import pip_setup

pip_setup.install("moviepy")
pip_setup.install("pygame")

import Menu
import pygame
from moviepy.editor import *
import random
from Settings import *
from Sprites import *
from Menu import *
import time
import numpy as np


class GAME :
    def __init__(self):
        #GAME ~initialisation~
        self.file = "highscore.txt"
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.background = pygame.image.load("background.png").convert()
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_music = pygame.mixer.Sound('bip_bip_bap_1.wav')
        self.menu_music = pygame.mixer.Sound('bip_bip_bop_V4.wav')
        self.gameover_music = pygame.mixer.Sound('bip_bip_bup.wav')
        self.menu_music.set_volume(0.5)
        self.game_music.set_volume(0.5)
        self.gameover_music.set_volume(0.5)

    def new_game(self):
        #GAME ~new_game~
        self.wave = 1
        self.shoot = False
        self.lastHitTimer = 0
        self.lastHitTimer_e  = 0
        self.lastHitennemyTimer = 0
        self.lastShootTimer = 0
        self.last_boss_attack = 0
        self.anim_jar = 0
        self.last_jar_attack = 0
        self.anim_player_attack = 0
        self.anim_ennemi_attack = 0
        self.boss_attack = False
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.ennemis = pygame.sprite.Group()
        self.weapons = pygame.sprite.Group()
        self.skulls = pygame.sprite.Group()
        self.jars = pygame.sprite.Group()
        self.fires = pygame.sprite.Group()
        self.player = PLAYER(self)
        self.ennemy_list = []
        self.all_sprites.add(self.player)
        self.ennemy_speed = 2
        self.ennemy_range = 400
        self.ennemy_attack = 30
        self.life_multiplyer = 0.4
        self.x_jar = round(PLATFORMS_LIST[0][0]) + 30
        for nbr in range(3):
            self.jar = JAR(self.platforms,(self.x_jar+(50*nbr)))
            self.jars.add(self.jar)
            self.all_sprites.add(self.jar)
        for nbr in range(3):
            self.dynamic_difficulty()
            ennemi = ENNEMI(random.randrange(self.ennemy_speed-1,self.ennemy_speed+1), self.ennemy_range, self.ennemy_attack, self.platforms, 0.5 , 1)
            self.ennemis.add(ennemi)
            self.all_sprites.add(ennemi)
            self.ennemy_list.append(ennemi)
        for plat in PLATFORMS_LIST:
            p = PLATFORM(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.weapon = WEAPON(1)
        self.weapons.add(self.weapon)
        self.all_sprites.add(self.weapon)
        self.skull = WEAPON(2)
        self.skulls.add(self.skull)
        self.all_sprites.add(self.skull)
        self.fire = WEAPON(3)
        self.fires.add(self.fire)
        self.all_sprites.add(self.fire)
        self.player.right = False
        self.attacked = False
        self.run()

    def run(self):
        #GAME ~loop~
        self.play = True
        while self.play:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            

    def update(self):
        # GAME ~update~
        self.all_sprites.update()

        #jar animation
        for self.jar in self.jars:
            if self.anim_jar < 8:
                self.jar.image = self.jar.sprites[int(self.anim_jar)]
                self.anim_jar = self.anim_jar + 0.05
            else : 
                self.anim_jar = 0

        #management of the artificial intelligence of the ennemies
        for ennemi in self.ennemis:
            ennemi.AI(self.player.pos, self.platforms)

        #gestion of the collision of the platform if falling
        plat_hits = pygame.sprite.spritecollide(self.player , self.platforms , False)
        if self.player.vel.y > 0:
            if plat_hits :
                #if the player is under the platform
                self.player.pos.y = plat_hits[0].rect.top
                self.player.vel.y = 0

        #gestion of the collision of the player and ennimies
        self.player_hits = pygame.sprite.spritecollide(self.player , self.ennemis , False)
        self.player_toutch = pygame.sprite.spritecollide(self.player , self.jars , False)
        self.player_toutch_fire = pygame.sprite.spritecollide(self.player , self.fires , False)
        if (pygame.time.get_ticks() < self.lastHitTimer + 1000):
            if self.player.right :
                self.player.image = self.player.sprites_attaqued[1]
            elif not self.player.right:
                self.player.image = self.player.sprites_attaqued[0]
        else:
            if self.player_hits or self.player_toutch or self.player_toutch_fire :
                if self.player.right :
                    self.player.image = self.player.sprites_attaqued[1]
                elif not self.player.right:
                    self.player.image = self.player.sprites_attaqued[0]
                self.lastHitTimer = pygame.time.get_ticks()
                self.player.life -= 1 
                self.player.pos.x -= 3


        for ennemi in self.ennemis:
            ennemi_hit_together = pygame.sprite.collide_rect(self.player, ennemi)
            if ennemi.right:
                self.ennemi_looking_at = 1
            else:
                self.ennemi_looking_at = -1
            if ennemi_hit_together and ennemi.type_en == 1:
                if ennemi.attack_anim < 10 and self.ennemi_looking_at == 1:
                    ennemi.image = ennemi.sprites_attack_right[int(ennemi.attack_anim)]
                    ennemi.attack_anim = ennemi.attack_anim + 0.3
                elif ennemi.attack_anim < 10 and self.ennemi_looking_at == -1:
                    ennemi.image = ennemi.sprites_attack_left[int(ennemi.attack_anim)]
                    ennemi.attack_anim = ennemi.attack_anim + 0.3
                else : 
                    ennemi.attack_anim = 0


            #

            #if ennemi_hit_together == 1 and (pygame.time.get_ticks() > self.lastHitennemyTimer + 100) and ennemi.isFalling == False:
                #ennemi.move(random.randint(-10, 10))
                #self.lastHitennemyTimer = pygame.time.get_ticks()
            ennemi_hits = pygame.sprite.spritecollide(ennemi , self.weapons , False)
            ennemi.life_multiplyer = self.life_multiplyer
            if ennemi.type_en == 1 and not self.player_hits:
                if (pygame.time.get_ticks() < self.lastHitTimer_e + 500) and  ennemi_hits  :
                    if ennemi.right :
                        ennemi.image = ennemi.sprites_walk[2]
                    elif not ennemi.right:
                        ennemi.image = ennemi.sprites_walk[3]
                else:
                    if ennemi.right :
                        ennemi.image = ennemi.sprites_walk[0]
                    elif not ennemi.right:
                        ennemi.image = ennemi.sprites_walk[1]
                    if ennemi_hits and self.player.pos.x > ennemi.rect.x and self.shoot :
                        if ennemi.right :
                            ennemi.image = ennemi.sprites_walk[2]
                        elif not ennemi.right:
                            ennemi.image = ennemi.sprites_walk[3]
                        self.lastHitTimer_e = pygame.time.get_ticks()
                        ennemi.life -= 1
                        if ennemi.isFalling == False:
                            ennemi.rect.x -= 10
                    elif ennemi_hits and self.player.pos.x < ennemi.rect.x and self.shoot:
                        if ennemi.right :
                            ennemi.image = ennemi.sprites_walk[2]
                        elif not ennemi.right:
                            ennemi.image = ennemi.sprites_walk[3]
                        self.lastHitTimer_e = pygame.time.get_ticks()
                        ennemi.life -= 1
                        if ennemi.isFalling == False:
                            ennemi.rect.x += 10

        for ennemi in self.ennemis:
            if (pygame.time.get_ticks() > self.lastHitTimer_e + 500) :
                if ennemi_hits and self.shoot and ennemi.type_en == 2:
                    if ennemi.right :
                        ennemi.life -= 1
                        ennemi.image = ennemi.sprites_walk_right[5]
                        self.lastHitTimer_e = pygame.time.get_ticks()
                    elif not ennemi.right:
                        ennemi.image = ennemi.sprites_walk_left[5]
                        ennemi.life -= 1
                        self.lastHitTimer_e = pygame.time.get_ticks()

            if ennemi.life < 0 :
                ennemi.kill()
                self.player.score += 1

        if len(self.ennemis) == 0:
            self.wave += 1
            self.new_wave()

        if self.shoot and self.looking_at == -1 :
            if self.anim_player_attack < 9 :
                self.player.image = self.player.sprites_attack[int(self.anim_player_attack)]
                self.anim_player_attack = self.anim_player_attack + 0.3
        if self.shoot and self.looking_at == 1 :
            if self.anim_player_attack < 9 :
                self.player.image = self.player.sprites_attack_r[int(self.anim_player_attack)]
                self.anim_player_attack = self.anim_player_attack + 0.3

        #gestion of shoot or attack
        if self.shoot : 
            if self.looking_at == -1 : 
                if self.x < self.x_max :
                    y = (-9.81 /( 2 * (self.v0 * self.v0) * (math.cos(self.alpha) * math.cos(self.alpha)) ) * (self.x*self.x)) + math.tan(self.alpha) * self.x + self.h
                    self.weapon.rect.midbottom = (self.coord_x  , self.h + (self.h - y))
                    self.x = self.x + 10
                    self.coord_x = self.coord_x - 20
                else:
                    self.shoot = False
                    self.x = ( (self.v0*self.v0) * ( math.sin (2*self.alpha)) ) / (2*9.81) 
                    self.coord_x = 0
            elif self.looking_at == 1 : 
                if self.x < self.x_max :
                    y = (-9.81 /( 2 * (self.v0 * self.v0) * (math.cos(self.alpha) * math.cos(self.alpha)) ) * (self.x*self.x)) + math.tan(self.alpha) * self.x + self.h
                    self.weapon.rect.midbottom = (self.coord_x  , self.h + (self.h - y)  )
                    self.x = self.x + 10
                    self.coord_x = self.coord_x + 20
                else :
                    self.shoot = False
                    self.x = ( (self.v0*self.v0) * ( math.sin (2*self.alpha)) ) / (2*9.81)
                    self.coord_x = 0


        else : 
            #player have weapon
            self.weapon.rect.midbottom = (20000,20000)

        for ennemi in self.ennemis:
            if ennemi.type_en == 2 and pygame.time.get_ticks() > self.last_boss_attack + 5000:
                self.last_boss_attack = pygame.time.get_ticks()
                self.boss_h = float(ennemi.rect.y) + 30
                self.boss_angle = 50.0  # en degres
                self.boss_alpha = float(self.boss_angle * 3.14 / 180.0)  # conversion en radian
                self.boss_v0 = 40.0
                self.boss_x_max = self.skull.shoot(self.boss_v0, self.boss_alpha, self.boss_h)
                self.boss_coord_x = ennemi.rect.x + 65
                self.boss_x = ((self.boss_v0 * 0) * (math.sin(2 * self.boss_alpha))) / (9.81)
                self.boss_attack = True
                if ennemi.right:
                    self.boss_looking_at = 1
                else:
                    self.boss_looking_at = -1

        if self.boss_attack:
            if self.boss_looking_at == -1:
                if self.boss_x < self.boss_x_max:
                    self.boss_y = (-9.81 / (2 * (self.boss_v0 * self.boss_v0) * (math.cos(self.boss_alpha) * math.cos(self.boss_alpha))) * (
                                               self.boss_x * self.boss_x)) + math.tan(
                        self.boss_alpha) * self.boss_x + self.boss_h
                    self.skull.rect.midbottom = (self.boss_coord_x, self.boss_h + (self.boss_h - self.boss_y))
                    self.boss_x = self.boss_x + 10
                    self.boss_coord_x = self.boss_coord_x - 10
                else:
                    self.boss_attack = False
                    self.anim_ennemi_attack = 0
                    self.boss_x = ((self.boss_v0 * self.boss_v0) * (math.sin(2 * self.boss_alpha))) / (2 * 9.81)
                    self.boss_coord_x = 0
            elif self.boss_looking_at == 1:
                if self.boss_x < self.boss_x_max:
                    self.boss_y = (-9.81 / (2 * (self.boss_v0 * self.boss_v0) * (
                                math.cos(self.boss_alpha) * math.cos(self.boss_alpha))) * (
                                               self.boss_x * self.boss_x)) + math.tan(
                        self.boss_alpha) * self.boss_x + self.boss_h
                    self.skull.rect.midbottom = (self.boss_coord_x, self.boss_h + (self.boss_h - self.boss_y))
                    self.boss_x = self.boss_x + 10
                    self.boss_coord_x = self.boss_coord_x + 10
                else:
                    self.boss_x = ((self.boss_v0 * self.boss_v0) * (math.sin(2 * self.boss_alpha))) / (2 * 9.81)
                    self.boss_coord_x = 0
                    self.boss_attack = False
                    self.anim_ennemi_attack = 0
        else:
            # boss have skull
            self.skull.rect.midbottom = (20000, 20000)

        for ennemi in self.ennemis:
            if ennemi.right:
                self.boss_looking_at = 1
            else:
                self.boss_looking_at = -1
            if self.boss_attack and self.boss_looking_at == -1 and ennemi.type_en == 2:
                if self.anim_ennemi_attack < 7:
                    ennemi.image = ennemi.sprites_attack_right[int(self.anim_ennemi_attack)]
                    self.anim_ennemi_attack = self.anim_ennemi_attack + 0.3
            if self.boss_attack and self.boss_looking_at == 1 and ennemi.type_en == 2:
                if self.anim_ennemi_attack < 7:
                    ennemi.image = ennemi.sprites_attack_left[int(self.anim_ennemi_attack)]
                    self.anim_ennemi_attack = self.anim_ennemi_attack + 0.3
            ennemi_hit_together = pygame.sprite.collide_rect(self.player, ennemi)
            if ennemi_hit_together and ennemi.type_en == 2:
                if ennemi.attack_anim_boss < 10 and self.boss_looking_at == -1:
                    ennemi.image = ennemi.sprites_boss_attack_right[int(ennemi.attack_anim_boss)]
                    ennemi.attack_anim_boss = ennemi.attack_anim_boss + 0.3
                elif ennemi.attack_anim_boss < 10 and self.boss_looking_at == 1:
                    ennemi.image = ennemi.sprites_boss_attack_left[int(ennemi.attack_anim_boss)]
                    ennemi.attack_anim_boss = ennemi.attack_anim_boss + 0.3
                else:
                    ennemi.attack_anim_boss = 0


        for jar in self.jars:
            if pygame.time.get_ticks() > self.last_jar_attack + 3000 :
                self.last_jar_attack = pygame.time.get_ticks()
                self.jar_h = float(jar.rect.y) + 50
                self.jar_angle = random.randint(7.0,11.0) # en degres
                self.jar_alpha = float(self.jar_angle * 3.14 / 180.0) #conversion en radian
                self.jar_v0 = random.randint(200,280)
                self.jar_x_max = self.skull.shoot(self.jar_v0, self.jar_alpha , self.jar_h)
                self.jar_coord_x = jar.rect.x + 65
                self.jar_x = ( (self.jar_v0*0) * ( math.sin (2*self.jar_alpha)) ) / (9.81)
                self.jar_attack = True


        if self.jar_attack:
            for self.jar in self.jars:
                if self.jar_x < self.jar_x_max :
                    self.jar_y = (-9.81 /( 2 * (self.jar_v0 * self.jar_v0) * (math.cos(self.jar_alpha) * math.cos(self.jar_alpha)) ) * (self.jar_x*self.jar_x)) + math.tan(self.jar_alpha) * self.jar_x + self.jar_h
                    self.fire.rect.midbottom = (self.jar_coord_x  , self.jar_h + (self.jar_h - self.jar_y)  )
                    self.jar_x = self.jar_x + 10
                    self.jar_coord_x = self.jar_coord_x + 3
                else :
                    self.jar_x = ( (self.jar_v0*self.jar_v0) * ( math.sin (2*self.jar_alpha)) ) / (2*9.81)
                    self.jar_coord_x = 0
                    self.jar_attack = False
        else : 
            #jar have skull
            self.fire.rect.midbottom = (20000,20000)



    def events(self):
        # GAME ~events~
        for event in pygame.event.get():
            #check if windows closed or game loose
            if event.type == pygame.QUIT :
                pygame.quit()
            if self.player.life <= 0 :
                if self.play:
                    self.play = False
                self.running = False

            #check if the player jump 
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    self.player.jump()

            #shoot 
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_e and pygame.time.get_ticks() > self.lastShootTimer + 300:
                    self.shoot = True
                    self.anim_player_attack = 0
                    self.h = float(self.player.pos.y)
                    if self.player.right:
                        self.looking_at = 1
                    else:
                        self.looking_at = -1
                    angle = 7.0 # en degres
                    self.alpha = float(angle * 3.14 / 180.0) #conversion en radian
                    self.v0 = 150.0
                    self.x_max = self.weapon.shoot(self.v0, self.alpha , self.h)
                    self.coord_x = self.player.pos.x
                    self.x = ( (self.v0*self.v0) * ( math.sin (2*self.alpha)) ) / (2*9.81)
                    self.lastShootTimer = pygame.time.get_ticks()
                if event.key == pygame.K_r:
                    self.attack = True


    def dynamic_difficulty(self):
        if pass_difficulty()==1:
            self.ennemy_speed=1
            self.ennemy_range=300
            self.ennemy_attack=25
            self.player.speed_multiplyer = 1
            self.life_multiplyer = 0.2
        if pass_difficulty()==2:
            self.ennemy_speed=2
            self.ennemy_range=400
            self.ennemy_attack=30
            self.life_multiplyer = 0.4
            self.player.speed_multiplyer = 1.2
        if pass_difficulty()==3:
            self.ennemy_speed=3
            self.ennemy_range=450
            self.ennemy_attack=4
            self.life_multiplyer = 0.6
            self.player.speed_multiplyer = 1.4
        if pass_difficulty()==4:
            self.ennemy_speed=4
            self.ennemy_range=600
            self.ennemy_attack=50
            self.life_multiplyer = 0.8
            self.player.speed_multiplyer = 1.6


    def new_wave(self):
        self.dynamic_difficulty()
        spawn_ennemi = 3
        nbr_ennemi = ((spawn_ennemi * self.wave)//2)
        for nbr in range(nbr_ennemi):
            ennemi = ENNEMI(random.randrange(self.ennemy_speed-1,self.ennemy_speed+1), self.ennemy_range, self.ennemy_attack, self.platforms,self.life_multiplyer, 1 )
            self.ennemis.add(ennemi)
            self.all_sprites.add(ennemi)
            self.ennemy_list.append(ennemi)
        if self.wave %3 == 0 :
            ennemi = ENNEMI(self.ennemy_speed//1.5, self.ennemy_range*3, self.ennemy_attack*2, self.platforms,self.life_multiplyer, 2 )
            self.ennemis.add(ennemi)
            self.all_sprites.add(ennemi)
            self.ennemy_list.append(ennemi)


    def draw(self):
        #GAME ~draw~
        self.screen.blit(self.background,(0,0))
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.wave), 40, BLACK, WIDTH / 2, 15)
        self.draw_text(str(self.player.life), 40, BLACK, WIDTH / 3, 15)

        #after drawing flip the display
        pygame.display.flip()

    def translate_difficulty(self):
        def easy():
            return "Easy"

        def normal():
            return "Normal"

        def hard():
            return "Hard"

        def nightmare():
            return "Nightmare"

        case = {1: easy,
                2: normal,
                3: hard,
                4: nightmare,
                }
        return case.get(pass_difficulty())()

    def add_data_to_highscore(self, f):
        with open(f, 'r') as file:  # we open the files in "read" mode
            data = file.readlines()
        self.username = input("Input your name : ")
        data.append(str(self.wave) + str(" ") + str(self.player.score) + str(" ") + str(self.translate_difficulty()) + str(" ") + str(self.username) + "\n")
        return data

    def add_data_to_highscore_temp(self, f):
        data = []
        data.append(str(self.wave) + str(" ") + str(self.player.score) + str(" ") + str(self.translate_difficulty()) + str(" ") + str(self.username) + "\n")
        return data

    def sort_highscore_data(self, f, data):
        l = len(data) - 1
        x = 0
        i = 0
        max_values = []
        index = 0
        while x < l:  # here i had to use a while as when the program deletes a line in data, the for wouldn't be updated and then the if would give an out of range error
            while data[x][i] != " ":
                i = i + 1
            max_values.append(data[x][:i] + "\n")
            i = 0
            x = x + 1
        if len(max_values) > 10:
            min1 = max_values[0]
            for i in range(len(max_values)):
                if max_values[i] < min1:
                    min1 = max_values[i]
                    index = i
            del data[index]
            del data[index]

        l = len(data)
        x = 0
        i = 0
        max_values = []
        index = 0
        while x < l:  # here i had to use a while as when the program deletes a line in data, the for wouldn't be updated and then the if would give an out of range error
            while data[x][i] != " ":
                i = i + 1
            max_values.append(data[x][:i])
            i = 0
            x = x + 1
        new_data = []
        alrsorted = 0
        len_values = len(max_values)
        while alrsorted < len_values:
            max = 0
            for i in range(len(max_values)):
                if int(max_values[i]) > int(max):
                    max = max_values[i]
                    index = i
            new_data.append(data[index])
            del max_values[index]
            del data[index]
            alrsorted = alrsorted + 1
        return new_data

    def add_highscore(self, f, highscore):
        file = open(f, "w")
        file.writelines(highscore)

    def show_start_screen(self):
        # GAME ~menu screen~
        self.menu_music.play(15,0,2500)
        menu(self)
        self.menu_music.set_volume(Menu.set_music())
        self.game_music.set_volume(Menu.set_music())
        self.gameover_music.set_volume(Menu.set_music())
        self.menu_music.fadeout(2500)
        self.game_music.play(15,0,2500)


    def show_game_over_screen(self):
        # GAME ~game over~
        self.add_highscore("highscore.txt",self.sort_highscore_data("highscore.txt", self.add_data_to_highscore("highscore.txt")))
        self.add_highscore(("highscore_temp.txt"),self.add_data_to_highscore_temp("highscore_temp.txt"))
        self.gameover_music.play(15,0,2500)
        self.game_music.fadeout(2500)
        game_over(self)
        self.gameover_music.fadeout(2500)

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('Arial', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)



movie = VideoFileClip("intro_v.2.3.mpg")
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
smallfont = pygame.font.SysFont('Corbel', 35)
text_loading = smallfont.render('Now loading...', True, WHITE)
screen.blit(text_loading,(WIDTH/2,HEIGHT/2))
movie.preview()

def launch_game():
    g = GAME()
    g.show_start_screen()

    while g.running:
        g.new_game()
        g.show_game_over_screen()
        launch_game()

launch_game()