import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 100)
red = (210, 50, 80)
green = (50, 170, 80)

width = 400
height = 400

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

ending_font = pygame.font.SysFont("Tahoma", 15)
score_font = pygame.font.SysFont("Tahoma", 25)

snake_block = 20
snake_speed = 15


def your_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    display.blit(value, [0, 0])


def the_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    msg = ending_font.render(msg, True, color)
    display.blit(msg, [width / 7, height / 2])


def game_loop():
    game_over = False
    game_close = False

    x_pos = width / 2
    y_pos = height / 2

    x_dir = 0
    y_dir = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

    food = [food_x, food_y]

    while not game_over:

        while game_close:
            display.fill(white)
            message("You Lost! Spacebar - Play Again OR Q - Quit", red)
            your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_dir = -snake_block
                    y_dir = 0
                elif event.key == pygame.K_RIGHT:
                    x_dir = snake_block
                    y_dir = 0
                elif event.key == pygame.K_UP:
                    y_dir = -snake_block
                    x_dir = 0
                elif event.key == pygame.K_DOWN:
                    y_dir = snake_block
                    x_dir = 0

        if x_pos >= width or x_pos < 0 or y_pos >= height or y_pos < 0:
            game_close = True

        x_pos += x_dir
        y_pos += y_dir
        display.fill(white)
        pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])
        head = [x_pos, y_pos]
        snake_list.append(head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == head:
                game_close = True

        the_snake(snake_block, snake_list)
        your_score(snake_length - 1)

        pygame.display.update()

        if head == food:
            food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            food = [food_x, food_y]
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
