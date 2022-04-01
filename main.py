import sys
import pygame
from level import Level
from setting import *

pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)


def debug(info, x=20, y=20):
    screen = pygame.display.get_surface()
    info_surf = font.render(str(info), True, "White")
    info_rect = screen.get_rect(topleft=(x, y))
    pygame.draw.rect(info_surf, "black", info_rect)
    screen.blit(info_surf, info_rect)


# join obj
level = Level()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

<<<<<<< HEAD
    screen.fill("blue")
=======
    screen.fill("black")
>>>>>>> a64ba96 (initㄉ)
    level.run()
    debug(level.player.dir)

    pygame.display.update()
    clock.tick(FPS)
