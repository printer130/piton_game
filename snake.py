import pygame
import time
import random
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis = pygame.display.set_mode((800, 800))

dis_height = 800
dis_width = 800

snake_block = 10

clock = pygame.time.Clock()
snake_speed = 10

def snake(snake_block, snake_list):
  for item in snake_list:
    pygame.draw.rect(dis, black, [int(item[0]), int(item[1]), snake_block, snake_block])

def msg(message, color):
  dis.blit(pygame.font.SysFont(None, 50).render(message, True, color), [int(dis_width/2), int(dis_height/2)])

def game():
  game_over = False
  game_close = False
  my_list = [1,2,3,4,5,6,7,8,9,123]

  x1_change = 0
  y1_change = 0

  x1 = dis_width / 2
  y1 = dis_height / 2

  snake_list = []
  len_of_snake = 1

  foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
  foody = round(random.randrange(0, dis_width - snake_block) / 10) * 10

  while not game_over:

    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        game_over = True
      if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_ESCAPE:
          game_over = True
        if e.key == pygame.K_UP:
          y1_change = -snake_block
          x1_change = 0
        if e.key == pygame.K_DOWN:
          y1_change = snake_block
          x1_change = 0
        if e.key == pygame.K_LEFT:
          y1_change = 0
          x1_change = -snake_block
        if e.key == pygame.K_RIGHT:
          y1_change = 0
          x1_change = snake_block

    if x1 < 0 or y1 < 0 or x1 >= dis_width or y1 >= dis_height:
      game_over = True

    x1 += x1_change
    y1 += y1_change

    dis.fill(white)
    pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_list.append(snake_Head)

    print(snake_list)
    if len(snake_list) > len_of_snake:
      del snake_list[0]

    for x in snake_list[:-1]:
      if x == snake_Head:
        game_over = True

    snake(snake_block, snake_list)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
      #asd
      foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
      foody = round(random.randrange(0, dis_width - snake_block) / 10) * 10
      len_of_snake += 1

    clock.tick(snake_speed)

  msg("Game over", red)
  pygame.display.update()
  # time.sleep(2)

  pygame.quit()
  quit()

game()