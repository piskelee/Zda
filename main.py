import sys
from level import Level
from setting import *
from tools import *

pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# join obj
level = Level()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")
    # join game_world
    level.run()
    pygame.display.update()
    clock.tick(FPS)
