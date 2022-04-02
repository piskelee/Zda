import pygame
from tools import import_csv_layout
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
        layouts = {
            "blocked": import_csv_layout("image/map/WORLD_MAP1_blocked.csv"),
            "road": import_csv_layout("image/map/WORLD_MAP1_road.csv")
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILE_SIZE
                        y = row_index * TILE_SIZE
                        if style == "blocked":
                            Tile((x, y), [self.o_sprite], "invisible")
                        # if style == "road":
                        #     Tile((x, y), [self.v_sprites, self.o_sprite], "invisible")
        #         if col == "x":
        #             Tile((x, y), [self.v_sprites, self.o_sprite])
        #         if col == "p":
        #             self.player = Player((x, y), [self.v_sprites], self.o_sprite)

        self.player = Player((160, 256), [self.v_sprites], self.o_sprite)

    def run(self):
        self.v_sprites.camera_draw(self.player)
        self.v_sprites.update()


class YCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        # get screen
        self.screen = pygame.display.get_surface()
        # offset
        self.half_width = self.screen.get_size()[0] // 2
        self.half_height = self.screen.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # draw floor
        self.floor = pygame.image.load("image/map/WORLD_MAP1.png").convert()
        self.floor_rect = self.floor.get_rect(topleft=(0, 0))

    def camera_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # draw floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.screen.blit(self.floor, floor_offset_pos)

        # sort and draw by y axis
        # for s in self.sprites():
        for s in sorted(self.sprites(), key=lambda s: s.rect.centery):
            offset_pos = s.rect.topleft - self.offset
            self.screen.blit(s.image, offset_pos)
