import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
GOLD = (255, 215, 0)
BLUE = (0, 0, 255)


FOOD_TYPES = [
    {"weight": 1, "color": RED, "timer": 10000},
    {"weight": 3, "color": GOLD, "timer": 5000},
    {"weight": 5, "color": BLUE, "timer": 3000}
]

font = pygame.font.SysFont("bahnschrift", 25)



def generate_food(snake_list):
    """Generate food not inside snake body"""
    food_type = random.choice(FOOD_TYPES)

    while True:
        x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

        if [x, y] not in snake_list:
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            spawn_time = pygame.time.get_ticks()
            return rect, food_type, spawn_time


def game_loop():
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    score = 0
    level = 1
    fps = 10

  
    food_rect, food_data, spawn_time = generate_food(snake_list)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

          
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = BLOCK_SIZE

        x += x_change
        y += y_change

        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            running = False

        screen.fill(BLACK)

        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

      
        for block in snake_list[:-1]:
            if block == snake_head:
                running = False

        
        for block in snake_list:
            pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

      
        current_time = pygame.time.get_ticks()

       
        if current_time - spawn_time > food_data["timer"]:
            food_rect, food_data, spawn_time = generate_food(snake_list)

      
        pygame.draw.rect(screen, food_data["color"], food_rect)

        
        snake_rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

        if snake_rect.colliderect(food_rect):
           
            score += food_data["weight"]

         
            snake_length += 1

        
            if score // 5 > level:
                level += 1
                fps += 2
              
            food_rect, food_data, spawn_time = generate_food(snake_list)

        text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(fps)


game_loop()
