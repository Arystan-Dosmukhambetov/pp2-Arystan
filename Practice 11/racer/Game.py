import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
SCORE = 0
COINS = 0

COIN_SPEED_STEP = 10

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

font_small = pygame.font.SysFont("Verdana", 20)

background = pygame.image.load("AnimatedStreet.png").convert()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load("Enemy.png").convert_alpha()
        self.image = pygame.transform.smoothscale(img, (60, 100))
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.spawn()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load("Player.png").convert_alpha()
        self.image = pygame.transform.smoothscale(img, (60, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, 520)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.weight = random.choice([1, 2, 5])

        img = pygame.image.load("coin.png").convert_alpha()

        size = 25 + self.weight * 5
        self.image = pygame.transform.smoothscale(img, (size, size))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group(P1, E1)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if random.randint(1, 60) == 1:
        c = Coin()
        coins.add(c)
        all_sprites.add(c)

    DISPLAYSURF.blit(background, (0, 0))

    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 140, SCREEN_HEIGHT - 30))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    collected = pygame.sprite.spritecollide(P1, coins, True)

    for coin in collected:
        COINS += coin.weight

    SPEED = 5 + (COINS // COIN_SPEED_STEP)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        font = pygame.font.SysFont("Verdana", 60)
        text = font.render("Game Over", True, BLACK)
        DISPLAYSURF.blit(text, (30, 250))

        pygame.display.update()
        time.sleep(2)

        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)