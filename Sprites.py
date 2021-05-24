# sprites classes

import pygame
from Settings import *
import random
import math
import time

vec = pygame.math.Vector2


class PLAYER(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        # import command of the game
        self.game = game

        self.sprites_walk_left = [pygame.image.load('don_cocorico_color_marche0.png'),
                                  pygame.image.load('don_cocorico_color_marche1.png'),
                                  pygame.image.load('don_cocorico_color_marche2.png'),
                                  pygame.image.load('don_cocorico_color_marche3.png'),
                                  pygame.image.load('don_cocorico_color_marche4.png'),
                                  pygame.image.load('don_cocorico_color_marche5.png')]
        self.sprites_walk_right = [pygame.image.load('don_cocorico_color_marche0_right.png'),
                                   pygame.image.load('don_cocorico_color_marche1_right.png'),
                                   pygame.image.load('don_cocorico_color_marche2_right.png'),
                                   pygame.image.load('don_cocorico_color_marche3_right.png'),
                                   pygame.image.load('don_cocorico_color_marche4_right.png'),
                                   pygame.image.load('don_cocorico_color_marche5_right.png')]
        self.sprites_attaqued = [pygame.image.load('don_cocorico_color_attaqued.png'),
                                 pygame.image.load('don_cocorico_color_attaqued_right.png')]
        self.sprites_attack = [pygame.image.load('don_cocorico_color_attack.png'),pygame.image.load('don_cocorico_color_attack2.png'),pygame.image.load('don_cocorico_color_attack3.png'),pygame.image.load('don_cocorico_color_attack4.png'),
        pygame.image.load('don_cocorico_color_attack4.png'),pygame.image.load('don_cocorico_color_attack3.png'),pygame.image.load('don_cocorico_color_attack2.png'),pygame.image.load('don_cocorico_color_attack.png'),pygame.image.load('don_cocorico_color_marche0.png')]
        self.sprites_attack_r = [pygame.image.load('don_cocorico_color_attack_r.png'),pygame.image.load('don_cocorico_color_attack2_r.png'),pygame.image.load('don_cocorico_color_attack3_r.png'),pygame.image.load('don_cocorico_color_attack4_r.png'),
        pygame.image.load('don_cocorico_color_attack4_r.png'),pygame.image.load('don_cocorico_color_attack3_r.png'),pygame.image.load('don_cocorico_color_attack2_r.png'),pygame.image.load('don_cocorico_color_attack_r.png'),pygame.image.load('don_cocorico_color_marche0_right.png')]
        # creat the player sprite ( rectangle )
        self.right = False
        self.current_sprite = 0
        if self.right:
            self.image = self.sprites_walk_right[self.current_sprite]
        elif not self.right:
            self.image = self.sprites_walk_left[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.life = 10
        self.speed_multiplyer = 1.2
        self.score = 0

    def jump(self):
        # jump only if the player is under a platform
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = - 20

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pygame.key.get_pressed()
        # check if the player is not in left side and left is choose
        if keys[pygame.K_LEFT] and self.pos.x >= 15 and not self.game.player_hits:
            self.right = False
            self.acc.x = -PLAYER_ACC * self.speed_multiplyer
            self.animation = True
            self.update_animation(self.sprites_walk_left)
        if keys[pygame.K_RIGHT] and not self.game.player_hits:
            self.right = True
            self.acc.x = PLAYER_ACC * self.speed_multiplyer
            self.animation = True
            self.update_animation(self.sprites_walk_right)

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # check if the player is in left side and left is choose
        if keys[pygame.K_LEFT] and self.pos.x <= 15:
            self.pos.x = 15
            self.acc.x = 0

        if keys[pygame.K_RIGHT] and self.pos.x >= WIDTH - 15:
            self.pos.x = WIDTH - 15
            self.acc.x = 0

        self.rect.midbottom = self.pos

    def update_animation(self, sprites):
        if self.animation == True:
            self.current_sprite += 0.2
            if int(self.current_sprite) >= len(sprites):
                self.current_sprite = 0
                self.animation = False
        self.image = sprites[int(self.current_sprite)]


class ENNEMI(pygame.sprite.Sprite):
    def __init__(self, c_Speed, c_dChase, c_dAttack, platforms, life_multiplyer, type_en):
        pygame.sprite.Sprite.__init__(self)

        # creat the ennemi sprite ( rectangle )
        self.attack_anim = 0
        self.attack_anim_boss = 0
        self.current_sprite = 0
        self.attack = False
        self.life = int(1 * life_multiplyer)
        self.right = False
        self.type_en = type_en
        if self.type_en == 1:
            self.sprites_walk = [pygame.image.load('Quetard_1.png'), pygame.image.load('Quetard_1_left.png'),
                                pygame.image.load('Quetard_1_attaqued.png'),
                                pygame.image.load('Quetard_1_attaqued_left.png')]
            self.sprites_attack_right = [pygame.image.load('Quetard_1.png'),pygame.image.load('Quetard_attack.png'), pygame.image.load('Quetard_attack2.png'),
                            pygame.image.load('Quetard_attack3.png'),
                            pygame.image.load('Quetard_attack4.png'),pygame.image.load('Quetard_attack4.png'), pygame.image.load('Quetard_attack3.png'),
                            pygame.image.load('Quetard_attack2.png'),
                            pygame.image.load('Quetard_attack.png'),pygame.image.load('Quetard_1.png')]
            self.sprites_attack_left = [pygame.image.load('Quetard_1_left.png'),pygame.image.load('Quetard_attack-l.png'), pygame.image.load('Quetard_attack2-l.png'),
                            pygame.image.load('Quetard_attack3-l.png'),
                            pygame.image.load('Quetard_attack4-l.png'),pygame.image.load('Quetard_attack4-l.png'), pygame.image.load('Quetard_attack3-l.png'),
                            pygame.image.load('Quetard_attack2-l.png'),
                            pygame.image.load('Quetard_attack-l.png'),pygame.image.load('Quetard_1_left.png')]
            self.life = int(5 * life_multiplyer)
            self.size = 100
            self.image = self.sprites_walk[0]
            self.rect = self.image.get_rect()
            self.plat = random.randint(1, 3)  # random.randint(0, len(PLATFORMS_LIST) - 1)
            self.rect.x = random.randint(round(PLATFORMS_LIST[self.plat][0]) + 10,
                                        round(PLATFORMS_LIST[self.plat][0] + PLATFORMS_LIST[self.plat][2]) - 40)
            self.rect.y = PLATFORMS_LIST[self.plat][1] - self.size
            self.plats = platforms

        if self.type_en == 2 :   
            self.sprites_walk_right = [pygame.image.load('Bunny1.png'), pygame.image.load('Bunny2.png'),
                                pygame.image.load('Bunny3.png'),
                                pygame.image.load('Bunny4.png'),pygame.image.load('Bunny.png'),pygame.image.load('Bunny_attaqued_r.png')]
            self.sprites_walk_left = [pygame.image.load('Bunny1_l.png'), pygame.image.load('Bunny2_l.png'),
                                pygame.image.load('Bunny3_l.png'),
                                pygame.image.load('Bunny4_l.png'),pygame.image.load('Bunny_l.png'),pygame.image.load('Bunny_attaqued.png')]
            self.sprites_attack_right = [pygame.image.load('lapin_lance_2.png'),pygame.image.load('lapin_lance_3.png'), pygame.image.load('lapin_lance_4.png'),
                            pygame.image.load('lapin_lance_4.png'),
                            pygame.image.load('lapin_lance_3.png'),pygame.image.load('lapin_lance_2.png'), pygame.image.load('Bunny.png')]
            self.sprites_attack_left = [pygame.image.load('lapin_lance_2_l.png'),pygame.image.load('lapin_lance_3_l.png'), pygame.image.load('lapin_lance_4_l.png'),
                            pygame.image.load('lapin_lance_4_l.png'),
                            pygame.image.load('lapin_lance_3_l.png'),pygame.image.load('lapin_lance_2_l.png'), pygame.image.load('Bunny_l.png')]
            self.sprites_boss_attack_right = [pygame.image.load('lapin_sabre_1.png'),pygame.image.load('lapin_sabre_2.png'), pygame.image.load('lapin_sabre_3.png'),
                            pygame.image.load('lapin_sabre_4.png'),
                            pygame.image.load('lapin_sabre_5.png'),pygame.image.load('lapin_sabre_6.png'), pygame.image.load('lapin_sabre_7.png'),pygame.image.load('lapin_sabre_7.png'),pygame.image.load('lapin_sabre_6.png'),
                            pygame.image.load('lapin_sabre_5.png') ,pygame.image.load('lapin_sabre_4.png') ,pygame.image.load('lapin_sabre_3.png'),pygame.image.load('lapin_sabre_2.png'),
                            pygame.image.load('lapin_sabre_1.png')]
            self.sprites_boss_attack_left = [pygame.image.load('lapin_sabre_1_l.png'),pygame.image.load('lapin_sabre_2_l.png'), pygame.image.load('lapin_sabre_3_l.png'),
                            pygame.image.load('lapin_sabre_4_l.png'),
                            pygame.image.load('lapin_sabre_5_l.png'),pygame.image.load('lapin_sabre_6_l.png'), pygame.image.load('lapin_sabre_7_l.png'),pygame.image.load('lapin_sabre_7_l.png'),pygame.image.load('lapin_sabre_6_l.png'),
                            pygame.image.load('lapin_sabre_5_l.png') ,pygame.image.load('lapin_sabre_4_l.png') ,pygame.image.load('lapin_sabre_3_l.png'),pygame.image.load('lapin_sabre_2_l.png'),
                            pygame.image.load('lapin_sabre_1_l.png')]

            self.life = int(10 * life_multiplyer)
            self.size = 160
            self.image = self.sprites_walk_right[0]
            self.rect = self.image.get_rect()
            self.plat = 0
            self.rect.x = random.randint(round(PLATFORMS_LIST[self.plat][0]) + 10,
                                        round(PLATFORMS_LIST[self.plat][0] + PLATFORMS_LIST[self.plat][2]) - 40)
            self.rect.y = PLATFORMS_LIST[self.plat][1] - self.size
            self.plats = platforms

        self.plat_hits = pygame.sprite.spritecollide(self, platforms, False)

        # stats ennemi
        self.speed = c_Speed
        self.dChase = c_dChase
        self.dAttack = c_dAttack

        # actions ennemi
        self.isFalling = False

    def move(self, mvt):
        self.rect.x += mvt
        if (self.rect.x > PLATFORMS_LIST[self.plat][0] + PLATFORMS_LIST[self.plat][2] or self.rect.x + mvt < \
                PLATFORMS_LIST[self.plat][0]):  # and not self.isJumping:
            if self.isFalling:
                self.rect.y += self.speed * 3
            self.isFalling = True
            if self.plat_hits:
                self.rect.y = self.plat_hits[0].rect[1] - self.size
                for i in range(len(PLATFORMS_LIST)):
                    if int(PLATFORMS_LIST[i][0]) == self.plat_hits[0].rect[0] and int(PLATFORMS_LIST[i][1]) == \
                            self.plat_hits[0].rect[1]:
                        self.plat = i
                        self.isFalling = False
                        break

    def chase(self, pPos, cSpeed):
        if round(pPos.x - self.rect.x) > 0:
            self.move(cSpeed)
            self.right = True
            if self.type_en == 2:
                self.animation = True
                self.update_animation(self.sprites_walk_left)
        elif round(pPos.x - self.rect.x) < 0:
            self.move(-cSpeed)
            self.right = False
            if self.type_en == 2:
                self.animation = True
                self.update_animation(self.sprites_walk_right)


    def AI(self, playerPos, platforms):
        self.plat_hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.isFalling:
            self.move(0)
        else:
            distTarget = round(math.sqrt(((self.rect.x - playerPos.x) ** 2) + ((self.rect.y - playerPos.y) ** 2)))
            if distTarget >= self.dChase:
                self.mvt = random.randint(-self.speed, self.speed)
                if self.rect.x + self.mvt <= (
                        PLATFORMS_LIST[self.plat][0] + PLATFORMS_LIST[self.plat][2] - 40) and self.rect.x + self.mvt >= \
                        PLATFORMS_LIST[self.plat][0] + 10:
                    self.move(self.mvt)
            elif distTarget >= self.dAttack and distTarget < self.dChase:
                self.chase(playerPos, self.speed)
            elif distTarget < self.dAttack:
                self.attack = True


    def update_animation(self, sprites):
        if self.animation == True:
            self.current_sprite += 0.2
            if int(self.current_sprite) >= 4:
                self.current_sprite = 0
                self.animation = False
        self.image = sprites[int(self.current_sprite)]


class PLATFORM(pygame.sprite.Sprite):

    # creat platform
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)

        # creat the platform sprite ( rectangle )
        self.image = pygame.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class WEAPON(pygame.sprite.Sprite):

    def __init__(self,type_w):
        pygame.sprite.Sprite.__init__(self)
        if type_w == 1:
            # creat the weapons sprite ( rectangle )
            self.image = pygame.image.load('bullet.png')
            self.rect = self.image.get_rect()
        if type_w == 2:
            self.image = pygame.image.load('skull.png')
            self.rect = self.image.get_rect()
        if type_w == 3:
            self.image = pygame.image.load('fire.png')
            self.rect = self.image.get_rect()

    def shoot(self, v0, alpha, h):

        # calcul the position of the bullet
        delta = (math.tan(alpha) * math.tan(alpha)) - 4 * h * (
                    (-9.81) / (2 * (v0 * v0) * ((math.cos(alpha) * math.cos(alpha)))))
        x1 = - (- math.tan(alpha) + math.sqrt(delta)) / (
                    2 * 9.81 / (2 * (v0 * v0) * (math.cos(alpha) * math.cos(alpha))))
        x2 = - (- math.tan(alpha) - math.sqrt(delta)) / (
                    2 * 9.81 / (2 * (v0 * v0) * (math.cos(alpha) * math.cos(alpha))))
        if x1 > x2:
            xmax = x1
        else:
            xmax = x2
        xmax = int(xmax)

        return xmax



class JAR(pygame.sprite.Sprite):

    # creat platform
    def __init__(self,platforms, x):
        pygame.sprite.Sprite.__init__(self)

        # creat the jar sprite ( rectangle )
        self.sprites = [pygame.image.load('jar1.png'),pygame.image.load('jar2.png'),pygame.image.load('jar3.png'),pygame.image.load('jar4.png'),
        pygame.image.load('jar4.png'),pygame.image.load('jar3.png'),pygame.image.load('jar2.png'),pygame.image.load('jar1.png')]
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.plat = 0
        self.rect.x = x 
        self.rect.y = PLATFORMS_LIST[self.plat][1] - 100