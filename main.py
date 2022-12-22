import random
import pygame
import sys
import pygame_menu
from copy import deepcopy
from random import choice, randrange


pygame.init()

timer = pygame.time.Clock()
bg_image = pygame.image.load("logo.jpg")
BACKGROUND_COLOR = (255, 229, 180)
GREEN = (154, 205, 50)
TEXT_COLOR = (0, 0, 0)
OBJECTS_COLOR = (0, 39, 9)
COUNT = 20
SIZE = 20

MARGiN = 0
size = [998, 977]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')
courier = pygame.font.SysFont('None', 72)

class Body_Of_Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Body_Of_Snake) and self.x == other.x and self.y == other.y

    def insider(self):
        return 0 <= self.x < SIZE and 0 <= self.y < SIZE


def draw_body_part(color, row, colums):
    pygame.draw.rect(screen, color,
                     [10 + colums * SIZE + MARGiN * (colums + 1),
                      20 + row * SIZE + MARGiN * (row + 1), SIZE, SIZE])
def start_the_game():
    def draw_apple():
        x = random.randint(0, COUNT - 1)
        y = random.randint(0, COUNT - 1)
        draw_apple = Body_Of_Snake(x, y)
        while draw_apple in snakes_body:
            draw_apple.x = random.randint(0, COUNT - 1)
            draw_apple.y = random.randint(0, COUNT - 1)
        return draw_apple


    snakes_body = [Body_Of_Snake(5, 5), Body_Of_Snake(5, 6), Body_Of_Snake(5, 7)]
    y = player_y = 0
    x = player_x = 1
    speed = 1
    total = 0
    apple = draw_apple()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and x != 0:
                    player_y = -1
                    player_x = 0
                elif event.key == pygame.K_DOWN and x != 0:
                    player_y = 1
                    player_x = 0
                elif event.key == pygame.K_LEFT and y != 0:
                    player_y = 0
                    player_x = -1
                elif event.key == pygame.K_RIGHT and y != 0:
                    player_y = 0
                    player_x = 1

        screen.fill(BACKGROUND_COLOR)
        text_total = courier.render(f"Level(Speed): {speed}", 0, TEXT_COLOR)

        screen.blit(text_total, (SIZE, SIZE + 500))

        text_speed = courier.render(f"Total: {total}", 0, TEXT_COLOR)

        screen.blit(text_speed, (SIZE + 500, SIZE + 500))
        for row in range(COUNT):
            for colums in range(COUNT):
                color = GREEN
                draw_body_part(color, row, colums)

        head = snakes_body[-1]
        if not head.insider():
            break

        draw_body_part(OBJECTS_COLOR, apple.x, apple.y)
        for body_part in snakes_body:
            draw_body_part(OBJECTS_COLOR, body_part.x, body_part.y)

        if apple == head:
            total += 1
            speed = total // 2 + 1
            snakes_body.append(apple)
            apple = draw_apple()

        y = player_y
        x = player_x

        new_head = Body_Of_Snake(head.x + y, head.y + x)

        if new_head in snakes_body:
            break

        snakes_body.append(new_head)

        snakes_body.pop(0)

        pygame.display.flip()
        timer.tick(5 + speed)

main_theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.set_background_color_opacity(0.4)
menu = pygame_menu.Menu(' ', 500, 300,
                       theme=main_theme)

menu.add.text_input('Name: ', default='Никита Сергеевич')
menu.add.button('Play', start_the_game)
menu.add.button('Exit', pygame_menu.events.EXIT)

while True:

    screen.blit(bg_image, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()
