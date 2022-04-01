import pygame
from setting import *
from sprites import Tile, Player


class Level:
    def __init__(self):
        # get screen
        self.screen = pygame.display.get_surface()
        # open groups
        self.v_sprites = YCamera()
        self.o_sprite = pygame.sprite.Group()
        # join obj
        self.player = None
        # open fun
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == "x":
                    Tile((x, y), [self.v_sprites, self.o_sprite])
                if col == "p":
                    self.player = Player((x, y), [self.v_sprites], self.o_sprite)

    def run(self):
        self.v_sprites.camera_draw(self.player)
        self.v_sprites.update()


class YCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.half_width = self.screen.get_size()[0] // 2
        self.half_height = self.screen.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def camera_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for s in self.sprites():
            offset_pos = s.rect.topleft - self.offset
            self.screen.blit(s.image, offset_pos)
