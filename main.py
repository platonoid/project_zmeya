import random
import pygame
import sys
import pygame_menu
from copy import deepcopy
from random import choice, randrange

pygame.init()

bg_image = pygame.image.load("logo.jpg")
FRAME_COLOR = (146, 110, 174)
BLUE = (204, 255, 255)
BOUNCE = (255, 255, 255)
RED = (244, 0, 0)
SNAKE_COLOR = (0, 0, 0)
HEADER_COLOR = (146, 110, 174)

COUNT_BLOCK = 20
SIZE_BLOCK = 20

MARGiN = 1
HEADER_MARGIN = 100
size = [998, 977]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36)

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def insider(self):
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y < SIZE_BLOCK

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def draw_block(color, row, colums):
    pygame.draw.rect(screen, color,
                     [10 + colums * SIZE_BLOCK + MARGiN * (colums + 1),
                      20 + row * SIZE_BLOCK + MARGiN * (row + 1), SIZE_BLOCK, SIZE_BLOCK])
def start_the_game():
    def draw_empty_block():
        x = random.randint(0, COUNT_BLOCK - 1)
        y = random.randint(0, COUNT_BLOCK - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_block:
            empty_block.x = random.randint(0, COUNT_BLOCK - 1)
            empty_block.y = random.randint(0, COUNT_BLOCK - 1)
        return empty_block


    snake_block = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    apple = draw_empty_block()
    d_row = buf_row = 0
    d_col = buf_col = 1
    total = 0
    speed = 1

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    buf_row = -1
                    buf_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    buf_row = 1
                    buf_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    buf_row = 0
                    buf_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    buf_row = 0
                    buf_col = 1

        screen.fill(FRAME_COLOR)

        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])
        text_total = courier.render(f"Total: {total}", 0, BOUNCE)

        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK + 500))

        text_speed = courier.render(f"Level(Speed): {speed}", 0, BOUNCE)

        screen.blit(text_speed, (SIZE_BLOCK + 300, SIZE_BLOCK + 500))

        for row in range(COUNT_BLOCK):
            for colums in range(COUNT_BLOCK):
                if (row + colums % 2) == 0:
                    color = BLUE
                else:
                    color = BLUE
                draw_block(color, row, colums)

        head = snake_block[-1]
        if not head.insider():
            print('ti moi crash')
            break

        draw_block(RED, apple.x, apple.y)
        for block in snake_block:
            draw_block(SNAKE_COLOR, block.x, block.y)

        if apple == head:
            total += 1
            speed = total // 5 + 1
            snake_block.append(apple)
            apple = draw_empty_block()

        d_row = buf_row

        d_col = buf_col

        new_head = SnakeBlock(head.x + d_row, head.y + d_col)

        if new_head in snake_block:
            print('crash yourself')
            break

        snake_block.append(new_head)

        snake_block.pop(0)

        pygame.display.flip()
        timer.tick(3 + speed)

main_theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.set_background_color_opacity(0.4)
menu = pygame_menu.Menu(' ', 500, 300,
                       theme=main_theme)

menu.add.text_input('Имя лоха :', default='Waltuh White')
menu.add.button('Играть', start_the_game)
menu.add.button('Выйти', pygame_menu.events.EXIT)

def exit_screen():
    screen.fill(pygame.Color('black'))
    text_rect = fnt2.render('GAME OVER', True, pygame.Color('darkorange')).get_rect(center=(750 / 2, 940 / 2))
    screen.blit(fnt2.render('GAME OVER', True, pygame.Color('darkorange')), text_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(60)

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
