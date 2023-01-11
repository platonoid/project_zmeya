import random
import pygame
import sys
import time
import pygame_menu
from copy import deepcopy
from random import choice, randrange


pygame.init()
pygame.mixer.music.load('brawl stars — candyland season theme (www.lightaudio.ru).mp3')
pygame.mixer.music.play(-1)
e = pygame.mixer.Sound('Звук ICQ_ ошибка.wav')
d = pygame.mixer.Sound('legkiy-gluhoy-hrust-vetki.wav')

timer = pygame.time.Clock()
bg_image = pygame.image.load("logo.jpg")
final_image = pygame.image.load("final.jpg")
BACKGROUND_COLOR = (255, 229, 180)
GREEN = (154, 205, 50)
TEXT_COLOR = (0, 0, 0)
OBJECTS_COLOR = (0, 39, 9)
COUNT = 20
SIZE = 20
clock = pygame.time.Clock()
FPS = 50
vol = 1.0
flPause = False
events = pygame.event.get()
colors = ['black', 'white', 'red', 'yellow', 'orange', 'green', 'blue', 'purple', 'pink', 'brown', 'grey']
backcolors = ['white', 'black', 'blue', 'green', 'red', 'yellow', 'red', 'orange', 'red', 'grey', 'white']
applecolors = ['black', 'white', 'red', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'red']
position = []

color = 'black'
backcolor = 'green'
applecolor = 'black'

MARGiN = 1
running = True
size = [998, 977]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')
score_font = pygame.font.SysFont("comicsansms", 72)


def play_bg_music(state):
    if state:
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.pause()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    global color
    global backcolor
    global applecolor
    intro_text = ["Правила:", "",
                  "1.Никому не доверять",
                  "2.Всегда держать нож в руке",
                  "3.Правило проекта разгром не задавать вопросов",
                  "4.Хавать яблоки",
                  "5.Не врезаться в стены",
                  "6.Не врезаться в себя",
                  "7. Никому не рассказывать о бойцовском клубе",
                  "",
                  "Управление:",""
                  "1.Движение ТОЛЬКО на WASD",
                  "",
                  "Для начала игры нажмите \"Пробел\""]

    fon = pygame.transform.scale(bg_image, (size))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    pygame.draw.rect(screen, 'black',
                     [600, 500, 305, 229])

    def draw_body_part(color, row, colums, russia=0):
        if russia == 0:
            pygame.draw.rect(screen, color,
                             [600 + colums * 75 + MARGiN * (colums + 1),
                              500 + row * 75 + MARGiN * (row + 1), 75, 75])
            position.append([600 + colums * 75 + MARGiN * (colums + 1), 600 + colums * 75 + MARGiN * (colums + 1) + 75,
                              500 + row * 75 + MARGiN * (row + 1), 500 + row * 75 + MARGiN * (row + 1) + 75])
        else:
            pygame.draw.rect(screen, color,
                             [600 + colums * 75 + MARGiN * (colums + 1),
                              500 + row * 75 + MARGiN * (row + 1) + j, 75, 25])

    string_rendered = font.render('Выберите цвет змейки(по умолчанию чёрный)', 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    screen.blit(string_rendered, (500, 450))

    for row in range(4):
        for colums in range(4):
            if row * 4 + colums <= 10:
                color = colors[row * 4 + colums]
                draw_body_part(color, row, colums)
            elif row * 4 + colums == 11:
                j = 0
                color = 'white'
                draw_body_part(color, row, colums, russia=1)
                j = 25
                color = 'blue'
                draw_body_part(color, row, colums, russia=1)
                j = 50
                color = 'red'
                draw_body_part(color, row, colums, russia=1)
                position.append(
                    [600 + colums * 75 + MARGiN * (colums + 1), 600 + colums * 75 + MARGiN * (colums + 1) + 75,
                     500 + row * 75 + MARGiN * (row + 1), 500 + row * 75 + MARGiN * (row + 1) + 75])
                color = 'black'

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in position:
                    if i[0] <= event.pos[0] <= i[1] and i[2] <= event.pos[1] <= i[3]:
                        po = position.index(i)
                        if po != 11:
                            color = colors[po]
                            backcolor = backcolors[po]
                            applecolor = applecolors[po]
                        else:
                            color = 'russia'

        pygame.display.flip()
        clock.tick(FPS)


start_screen()


class Body_Of_Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Body_Of_Snake) and self.x == other.x and self.y == other.y

    def insider(self):
        return 0 <= self.x < SIZE and 0 <= self.y < SIZE

c = 0
def draw_body_part(color, row, colums, eto='pofig'):
    global c
    if color != 'russia':
        pygame.draw.rect(screen, color,
                         [10 + colums * SIZE + MARGiN * (colums + 1),
                          20 + row * SIZE + MARGiN * (row + 1), SIZE, SIZE])
    else:
        c += 1
        if eto == 'pole':
            pygame.draw.rect(screen, color,
                             [10 + colums * SIZE + MARGiN * (colums + 1),
                              20 + row * SIZE + MARGiN * (row + 1), SIZE, SIZE])
        elif eto == 'app':
            pygame.draw.rect(screen, 'blue',
                             [10 + colums * SIZE + MARGiN * (colums + 1),
                              20 + row * SIZE + MARGiN * (row + 1), SIZE, SIZE // 6])
            pygame.draw.rect(screen, 'white',
                             [10 + colums * SIZE + MARGiN * (colums + 1),
                              20 + row * SIZE + MARGiN * (row + 1) + SIZE // 6, SIZE, SIZE // 3])
            pygame.draw.rect(screen, 'red',
                             [10 + colums * SIZE + MARGiN * (colums + 1),
                              20 + row * SIZE + MARGiN * (row + 1) + SIZE // 6 * 5, SIZE, SIZE // 6])
        else:
            if c % 3 == 1:
                pygame.draw.rect(screen, 'white',
                                 [10 + colums * SIZE + MARGiN * (colums + 1),
                                  20 + row * SIZE + MARGiN * (row + 1), SIZE, SIZE])
            elif c % 3 == 2:
                pygame.draw.rect(screen, 'blue',
                                 [10 + colums * SIZE + MARGiN * (colums + 1),
                                  20 + row * SIZE + MARGiN * (row + 1), SIZE, SIZE])
            if c % 3 == 0:
                pygame.draw.rect(screen, 'red',
                                 [10 + colums * SIZE + MARGiN * (colums + 1),
                                  20 + row * SIZE + MARGiN * (row + 1), SIZE, SIZE])


def draw_apple():
    x = random.randint(0, COUNT - 1)
    y = random.randint(0, COUNT - 1)
    draw_apple = Body_Of_Snake(x, y)
    while draw_apple in snakes_body:
        draw_apple.x = random.randint(0, COUNT - 1)
        draw_apple.y = random.randint(0, COUNT - 1)
    return draw_apple

def message(msg,color):
    mesg = score_font.render(msg, True, color)
    screen.blit(mesg, [450, 320])


snakes_body = [Body_Of_Snake(5, 5), Body_Of_Snake(5, 6), Body_Of_Snake(5, 7)]
x = player_x = 0
y = player_y = 1
speed = 1
total = 0
apple = draw_apple()

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = my_font.render(
        'Your Total is : ' + str(total), True, applecolor)

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (450, 450)

    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    pygame.quit()

    quit()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            timer.tick(100000000)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and x != 0:
                player_x, player_y = 0, -1
            elif event.key == pygame.K_d and x != 0:
                player_x, player_y = 0, 1
            elif event.key == pygame.K_w and y != 0:
                player_x, player_y = -1, 0
            elif event.key == pygame.K_s and y != 0:
                player_x, player_y = 1, 0
    screen.fill(BACKGROUND_COLOR)
    text_total = score_font.render(f"Level(Speed): {speed}", 0, TEXT_COLOR)
    screen.blit(text_total, (SIZE, SIZE + 500))
    text_speed = score_font.render(f"Total: {total}", 0, TEXT_COLOR)
    screen.blit(text_speed, (SIZE + 600, SIZE + 500))
    for row in range(COUNT):
        for colums in range(COUNT):
            if color != 'russia':
                draw_body_part(backcolor, row, colums)
            else:
                if row <= COUNT // 2 - 1:
                    draw_body_part('darkblue', row, colums, eto='pole')
                else:
                    draw_body_part('yellow', row, colums, eto='pole')

    head = snakes_body[-1]
    if not head.insider():
        d.play()
        game_over()

    draw_body_part(applecolor, apple.y, apple.x, eto='app') # цвет яблока
    for body_part in snakes_body:
        draw_body_part(color, body_part.y, body_part.x, eto='snake') # цвет змейки


    if apple == head:
        total += 10
        speed = total // 20 + 1
        snakes_body.append(apple)
        apple = draw_apple()
        e.play()

    y = player_y
    x = player_x

    new_head = Body_Of_Snake(head.x + y, head.y + x)

    if new_head in snakes_body:
        d.play()
        game_over()

    snakes_body.append(new_head)
    snakes_body.pop(0)
    pygame.display.flip()
    timer.tick(5 + speed)