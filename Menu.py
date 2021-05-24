

import pygame
import random
from Settings import *
from Sprites import *
import os
import time

colors = [(252, 92, 101), (253, 150, 68), (254, 211, 48), (38, 222, 129), (235, 59, 90), (250, 130, 49),
          (247, 183, 49), (32, 191, 107), (15, 185, 177), (69, 170, 242), (75, 123, 236), (165, 94, 234),
          (119, 140, 163), (45, 152, 218), (56, 103, 214), (136, 84, 208), (165, 177, 194), (75, 101, 132)]


def random_color():
    nbr = random.randint(0, len(colors) - 1)  # have a random number
    return colors[nbr]  # return the random color

color_button_1 = random_color()
color_button_2 = random_color()
color_button_3 = random_color()
color_button_4 = random_color()
color_button_5 = random_color()

def menu(game):
    # light shade of the button and dark shade of the button
    color_light = (170,170,170)
    menu_titletest = pygame.image.load("background.png")
    menu_background1 = pygame.image.load("background_easy.png")
    menu_background2 = pygame.image.load("background_normal.png")
    menu_background3 = pygame.image.load("background_hard.png")
    menu_background4 = pygame.image.load("background_nightmare.png")
    game.screen.blit(menu_titletest, (0, 0))
    menu_settings_background = pygame.image.load("background.png")
    play_button = pygame.image.load("play_button.png")
    quit_button = pygame.image.load("quit_button.png")
    settings_button = pygame.image.load("settings_button.png")
    difficulty_button = pygame.image.load("difficulty_button.png")
    return_button = pygame.image.load("return_button.png")
    easy_button = pygame.image.load("easy_button.png")
    normal_button = pygame.image.load("normal_button.png")
    hard_button = pygame.image.load("hard_button.png")
    nightmare_button = pygame.image.load("nightmare_button.png")
    controls_button = pygame.image.load("controls_button.png")
    volume_button = pygame.image.load("volume_button.png")
    width = game.screen.get_width()
    height = game.screen.get_height()
    global selected_difficulty
    selected_difficulty=2
    global music_volume
    music_volume = 0.5


    # stores the (x,y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()
    global Main_menu
    global Settings_menu
    Main_menu = True
    Settings_menu = False
    Difficulty_menu = False
    while True :
        while Main_menu:
            for event in pygame.event.get():
            #checks if a mouse is clicked
                if event.type == pygame.QUIT :
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                #if the mouse is clicked on a button
                    if width/2 - 250 <= mouse[0] <= width/2+250 and height/1.7 <= mouse[1] <= height/1.7+60:
                        pygame.quit()
                    if width/2 - 250 <= mouse[0] <= width/2+250 and height/1.965 <= mouse[1] <= height/1.965+60:
                        return
                    if width/2 -250 <= mouse[0] <= width/2+250 and height/1.5<= mouse[1] <= height/1.5+60:
                        Main_menu = False
                        game.screen.blit(menu_settings_background, (0, 0))
                        Settings_menu = True
            mouse = pygame.mouse.get_pos()
            if selected_difficulty == 2:
                 game.screen.fill((0, 0, 0))
                 game.screen.blit(menu_background2, (0, 0))
            elif selected_difficulty == 1:
                 game.screen.fill((0, 0, 0))
                 game.screen.blit(menu_background1, (0, 0))
            elif selected_difficulty == 3:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background3, (0, 0))
            else:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background4, (0, 0))

        # if mouse is hovered on a button it changes to lighter shade
            if width/2-250 <= mouse[0] <= width/2+250 and height/1.965 <= mouse[1] <= height/1.965+60:
                pygame.draw.rect(game.screen,color_light,[width/2 - 260,height/2,520,70])
                game.screen.blit(play_button , [width/2 - 250,height/1.965,500,60])
            else:
                game.screen.blit(play_button , [width/2 - 250,height/1.965,500,60])

            if width/2-250 <= mouse[0] <= width/2+250 and height/1.7 <= mouse[1] <= height/1.7+60:
                pygame.draw.rect(game.screen,color_light,[width/2 - 260,height/1.72,520,70])
                game.screen.blit(quit_button,[width/2 - 250,height/1.7,500,60])
            else :
                game.screen.blit(quit_button,[width/2 - 250,height/1.7,500,60])

            if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.5 <= mouse[1] <= height / 1.5 + 60:
                pygame.draw.rect(game.screen, color_light, [width / 2 - 260, height / 1.51, 520, 70])
                game.screen.blit(settings_button,[width/2 - 250,height/1.5,500,60])
            else:
                game.screen.blit(settings_button,[width/2 - 250,height/1.5,500,60])
        #pygame.draw.rect(game.screen, color_dark, [width / 2, height / 9, 10, 900])

        # updates the frames of the game
            pygame.display.update()

        while Settings_menu:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                #if the mouse is clicked on a button
                    if width/2 - 250 <= mouse[0] <= width/2+250 and height/1.342 <= mouse[1] <= height/1.342+60:
                        Main_menu = True
                        Settings_menu = False
                    if width/2 - 250 <= mouse[0] <= width/2+250 and height/1.965 <= mouse[1] <= height/1.965+60:
                        Settings_menu = False
                        Difficulty_menu = True
                    if width / 2 - 250 <= mouse[0] <= width / 2 - 150 and height / 1.5 <= mouse[1] <= height / 1.5 + 60:
                        music_volume = 0.2
                    if width / 2 + 150 <= mouse[0] <= width / 2 + 250 and height / 1.5 <= mouse[1] <= height / 1.5 + 60:
                        music_volume = 0.7
                    if width / 2 - 150 <= mouse[0] <= width / 2 + 150 and height / 1.5 <= mouse[1] <= height / 1.5 + 60:
                        music_volume = 0
            mouse = pygame.mouse.get_pos()
            if selected_difficulty == 2:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background2, (0, 0))
            elif selected_difficulty == 1:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background1, (0, 0))
            elif selected_difficulty == 3:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background3, (0, 0))
            else:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background4, (0, 0))

            if width/2-250 <= mouse[0] <= width/2+250 and height/1.965 <= mouse[1] <= height/1.965+60:
                pygame.draw.rect(game.screen,color_light,[width/2 - 260,height/2,520,70])
                game.screen.blit(difficulty_button, [width/2 - 250,height/1.965,500,60])
            else:
                game.screen.blit(difficulty_button, [width/2 - 250,height/1.965,500,60])

            if width/2-250 <= mouse[0] <= width/2+250 and height/1.7 <= mouse[1] <= height/1.7+60:
                pygame.draw.rect(game.screen,color_light,[width/2 - 260,height/1.72,520,70])
                game.screen.blit(controls_button,[width/2 - 250,height/1.7,500,60])
                fontsettings = pygame.font.SysFont('Corbel', 33)
                text_controls1 = fontsettings.render('Press E to shoot', True, GREEN)
                text_controls2 = fontsettings.render('Press -> to go right', True, GREEN)
                text_controls3 = fontsettings.render('Press <- to go left', True, GREEN)
                text_controls4 = fontsettings.render('Press space to jump', True, GREEN)
                game.screen.blit(text_controls1, (width / 2 - 100, 200))
                game.screen.blit(text_controls2, (width / 2 - 100, 250))
                game.screen.blit(text_controls3, (width / 2 - 100, 300))
                game.screen.blit(text_controls4, (width / 2 - 100, 350))
            else :
                game.screen.blit(controls_button,[width/2 - 250,height/1.7,500,60])

            if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.5 <= mouse[1] <= height / 1.5 + 60:
                pygame.draw.rect(game.screen, color_light, [width / 2 - 260, height / 1.515, 520, 70])
                game.screen.blit(volume_button,[width/2 - 250,height/1.5,500,60])
            else:
                game.screen.blit(volume_button,[width/2 - 250,height/1.5,500,60])

            if width/2-250 <= mouse[0] <= width/2+250 and height/1.342 <= mouse[1] <= height/1.342+60:
                pygame.draw.rect(game.screen,color_light,[width/2 - 260,height/1.35,520,70])
                game.screen.blit(return_button,[width/2 - 250,height/1.342,500,60])
            else :
                game.screen.blit(return_button,[width/2 - 250,height/1.342,500,60])

            pygame.display.update()

        while Difficulty_menu :
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                #if the mouse is clicked on a button
                    if width/2 - 250 <= mouse[0] <= width/2+250 and height/1.213 <= mouse[1] <= height/1.213+60:
                        game.screen.fill((0, 0, 0))
                        game.screen.blit(menu_settings_background, (0, 0))
                        Settings_menu = True
                        Difficulty_menu = False
                    if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.965 <= mouse[1] <= height / 1.965 + 60:
                        selected_difficulty = 1
                        game.screen.fill((0, 0, 0))
                        game.screen.blit(menu_settings_background, (0, 0))
                        Settings_menu = False
                        Difficulty_menu = False
                        Main_menu = True
                    if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.7 <= mouse[1] <= height / 1.7 + 60:
                        selected_difficulty=2
                        game.screen.fill((0, 0, 0))
                        game.screen.blit(menu_settings_background, (0, 0))
                        Settings_menu = False
                        Difficulty_menu = False
                        Main_menu = True
                    if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.5 <= mouse[1] <= height / 1.5 + 60:
                        game.screen.fill((0, 0, 0))
                        game.screen.blit(menu_settings_background, (0, 0))
                        Settings_menu = False
                        Difficulty_menu = False
                        Main_menu = True
                        selected_difficulty = 3
                    if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.342 <= mouse[1] <= height / 1.342 + 60:
                        selected_difficulty = 4
                        game.screen.fill((0, 0, 0))
                        game.screen.blit(menu_settings_background, (0, 0))
                        Settings_menu = False
                        Difficulty_menu = False
                        Main_menu = True
            mouse = pygame.mouse.get_pos()
            if selected_difficulty == 2:
                 game.screen.fill((0, 0, 0))
                 game.screen.blit(menu_background2, (0, 0))
            elif selected_difficulty == 1:
                 game.screen.fill((0, 0, 0))
                 game.screen.blit(menu_background1, (0, 0))
            elif selected_difficulty == 3:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background3, (0, 0))
            else:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background4, (0, 0))

            if width/2-250 <= mouse[0] <= width/2+250 and height/1.965 <= mouse[1] <= height/1.965+60:
                pygame.draw.rect(game.screen,color_light,[width/2 - 260,height/2,520,70])
                game.screen.blit(easy_button , [width/2 - 250,height/1.965,500,60])
            else:
                game.screen.blit(easy_button , [width/2 - 250,height/1.965,500,60])

            if width/2-250 <= mouse[0] <= width/2+250 and height/1.7 <= mouse[1] <= height/1.7+60:
                pygame.draw.rect(game.screen,color_light,[width/2 - 260,height/1.72,520,70])
                game.screen.blit(normal_button,[width/2 - 250,height/1.7,500,60])
            else :
                game.screen.blit(normal_button,[width/2 - 250,height/1.7,500,60])

            if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.5 <= mouse[1] <= height / 1.5 + 60:
                pygame.draw.rect(game.screen, color_light, [width / 2 - 260, height / 1.515, 520, 70])
                game.screen.blit(hard_button,[width/2 - 250,height/1.5,500,60])
            else:
                game.screen.blit(hard_button,[width/2 - 250,height/1.5,500,60])

            if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.342 <= mouse[1] <= height / 1.342 + 60:
                pygame.draw.rect(game.screen, color_light, [width / 2 - 260, height / 1.35, 520, 70])
                game.screen.blit(nightmare_button,[width/2 - 250,height/1.342,500,60])
            else:
                game.screen.blit(nightmare_button,[width/2 - 250,height/1.342,500,60])

            if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.213 <= mouse[1] <= height / 1.213 + 60:
                pygame.draw.rect(game.screen, color_light, [width / 2 - 260, height / 1.22, 520, 70])
                game.screen.blit(return_button,[width/2 - 250,height/1.213,500,60])
            else:
                game.screen.blit(return_button,[width/2 - 250,height/1.213,500,60])

            pygame.display.update()


def set_music():
    def mute():
        return 0

    def low():
        return 0.2

    def medium():
        return 0.5

    def high():
        return 0.7

    case = {0: mute,
            0.2: low,
            0.5: medium,
            0.7: high
            }
    return case.get(music_volume)()

def pass_difficulty():
    return selected_difficulty

f = "highscore.txt"
f_new = "highscore_temp.txt"

def translate_highscore_new(f):
    with open(f, 'r') as file:  # we open the files in "read" mode
        data = file.readlines()
    new_data = []
    x = 0
    i = 0
    while data[x][i] != " ":
        i = i + 1
    wave = str(data[x][:i])
    j = i + 1
    while data[x][j] != " ":
        j = j + 1
    score = str(data[x][i:j])
    k = j + 1
    while data[x][k] != " ":
        k = k + 1
    difficulty = str(data[x][j:k])
    l = k + 1
    while data[x][l] != "\n":
        l = l + 1
    username = str(data[x][k:l])
    new_data.append(username + " survived until wave " + wave + " and had a score of " + score + " with the " + difficulty + " difficulty")
    return new_data

def translate_highscore(f):
    with open(f, 'r') as file:  # we open the files in "read" mode
            data = file.readlines()
    new_data = []
    x = 0
    i = 0
    while x < len(data):  # here i had to use a while as when the program deletes a line in data, the for wouldn't be updated and then the if would give an out of range error
        while data[x][i] != " ":
            i = i + 1
        wave = str(data[x][:i])
        j = i + 1
        while data[x][j] != " ":
            j = j + 1
        score = str(data[x][i:j])
        k = j + 1
        while data[x][k] != " ":
            k = k + 1
        difficulty = str(data[x][j:k])
        l = k + 1
        while data[x][l] != "\n":
            l = l + 1
        username = str(data[x][k:l])
        x = x + 1
        new_data.append(username + " survived until wave " + wave + " and had a score of " + score + " with the " + difficulty + " difficulty")
    return new_data


def game_over(game):
    menu_background1 = pygame.image.load("background_easy.png")
    menu_background2 = pygame.image.load("background_normal.png")
    menu_background3 = pygame.image.load("background_hard.png")
    menu_background4 = pygame.image.load("background_nightmare.png")
    replay_button = pygame.image.load("replay_button.png")
    highscore_button = pygame.image.load("highscore_button.png")
    quit_button = pygame.image.load("quit_button.png")
    global game_over_menu
    global highscore_menu
    highscore_menu = False
    game_over_menu = True
    while True :
        while game_over_menu:
            mouse = pygame.mouse.get_pos()
            width = game.screen.get_width()
            height = game.screen.get_height()
            color_light = (170,170,170)

            for event in pygame.event.get():
                # checks if a mouse is clicked
                if event.type == pygame.QUIT :
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if the mouse is clicked on a button
                    if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.5 <= mouse[1] <= height / 1.5 + 60:
                        game_over_menu = False
                        highscore_menu = True
                    if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.213 <= mouse[1] <= height / 1.213 + 60:
                        pygame.quit()
                    if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.342 <= mouse[1] <= height / 1.342 + 60:
                        return
            mouse = pygame.mouse.get_pos()
            if selected_difficulty == 2:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background2, (0, 0))
            elif selected_difficulty == 1:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background1, (0, 0))
            elif selected_difficulty == 3:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background3, (0, 0))
            else:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background4, (0, 0))

            if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.5 <= mouse[1] <= height / 1.5 + 60:
                pygame.draw.rect(game.screen, color_light, [width / 2 - 260, height / 1.515, 520, 70])
                game.screen.blit(highscore_button, [width / 2 - 250, height / 1.5, 500, 60])
            else:
                game.screen.blit(highscore_button, [width / 2 - 250, height / 1.5, 500, 60])

            if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.342 <= mouse[1] <= height / 1.342 + 60:
                pygame.draw.rect(game.screen, color_light, [width / 2 - 260, height / 1.35, 520, 70])
                game.screen.blit(replay_button, [width / 2 - 250, height / 1.342, 500, 60])
            else:
                game.screen.blit(replay_button, [width / 2 - 250, height / 1.342, 500, 60])

            if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.213 <= mouse[1] <= height / 1.213 + 60:
                pygame.draw.rect(game.screen, color_light, [width / 2 - 260, height / 1.22, 520, 70])
                game.screen.blit(quit_button, [width / 2 - 250, height / 1.213, 500, 60])
            else:
                game.screen.blit(quit_button, [width / 2 - 250, height / 1.213, 500, 60])

            size_score = (translate_highscore_new(f_new))
            i = 0
            fontsettings = pygame.font.SysFont('Corbel', 33)
            while i < len(size_score) :
                text_highscore = fontsettings.render(size_score[i], True, BLACK)
                game.screen.blit(text_highscore, (width / 2 - 400, height / (2 - (0.1 * i)) + 15))
                i = i + 1

            pygame.display.update()
        while highscore_menu :
            mouse = pygame.mouse.get_pos()
            width = game.screen.get_width()
            height = game.screen.get_height()
            color_light = (170, 170, 170)

            for event in pygame.event.get():
                # checks if a mouse is clicked
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if the mouse is clicked on a button
                    if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.213 <= mouse[1] <= height / 1.213 + 60:
                        pygame.quit()
                    if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.342 <= mouse[1] <= height / 1.342 + 60:
                        return
            mouse = pygame.mouse.get_pos()
            if selected_difficulty == 2:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background2, (0, 0))
            elif selected_difficulty == 1:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background1, (0, 0))
            elif selected_difficulty == 3:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background3, (0, 0))
            else:
                game.screen.fill((0, 0, 0))
                game.screen.blit(menu_background4, (0, 0))

            if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.342 <= mouse[1] <= height / 1.342 + 60:
                pygame.draw.rect(game.screen, color_light, [width / 2 - 260, height / 1.35, 520, 70])
                game.screen.blit(replay_button, [width / 2 - 250, height / 1.342, 500, 60])
            else:
                game.screen.blit(replay_button, [width / 2 - 250, height / 1.342, 500, 60])

            if width / 2 - 250 <= mouse[0] <= width / 2 + 250 and height / 1.213 <= mouse[1] <= height / 1.213 + 60:
                pygame.draw.rect(game.screen, color_light, [width / 2 - 260, height / 1.22, 520, 70])
                game.screen.blit(quit_button, [width / 2 - 250, height / 1.213, 500, 60])
            else:
                game.screen.blit(quit_button, [width / 2 - 250, height / 1.213, 500, 60])

            size_score = (translate_highscore(f))
            i = 0
            fontsettings = pygame.font.SysFont('Corbel', 33)
            while i < 10 :
                text_highscore = fontsettings.render(size_score[i], True, GREEN)
                game.screen.blit(text_highscore, (width / 2 - 450, 70 + (50 * i)))
                i = i + 1

            pygame.display.update()
