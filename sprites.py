import pygame
from setting import *


class SpriteSheet:
    def __init__(self, img):
        self.img = img

    def get_image(self, frame_x, frame_y, img_width, img_height, scale):
        img = pygame.Surface((img_width, img_height)).convert_alpha()
        img.blit(self.img, (0, 0), ((frame_x * img_width), (frame_y * img_height), img_width, img_height))
        img = pygame.transform.scale(img, (img_width * scale, img_height * scale))
        return img


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILE_SIZE, TILE_SIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        # image
        self.image = surface
        self.image.fill("green")
        # rect
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -12)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, o_sprites):
        super().__init__(groups)
        # image
        self.image = pygame.image.load("image/player/player.png").convert_alpha()
        self.dir_left = []
        self.dir_right = []
        self.dir_up = []
        self.dir_down = []
        self.dir_idel = []
        # rect
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)
        # moving
        self.dir = pygame.math.Vector2()
        self.speed = 2

        self.o_sprites = o_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        # x axis
        if keys[pygame.K_d]:
            self.dir.x = 1
        elif keys[pygame.K_a]:
            self.dir.x = -1
        else:
            self.dir.x = 0
        # y axis
        if keys[pygame.K_s]:
            self.dir.y = 1
        elif keys[pygame.K_w]:
            self.dir.y = -1
        else:
            self.dir.y = 0

    def collision(self, dir):
        if dir == "h":
            for s in self.o_sprites:
                if s.rect.colliderect(self.rect):
                    if self.dir.x > 0:  # moving right
                        self.rect.right = s.rect.left
                    if self.dir.x < 0:  # moving lefgt
                        self.rect.left = s.rect.right

        if dir == "v":
            for s in self.o_sprites:
                if s.rect.colliderect(self.rect):
                    if self.dir.y > 0:  # moving down
                        self.rect.bottom = s.rect.top
                    if self.dir.y < 0:  # moving up
                        self.rect.top = s.rect.bottom

    def move(self, speed):
        if self.dir.magnitude() != 0:
            self.dir = self.dir.normalize()

        self.rect.x += self.dir.x * speed
        self.collision("h")

        self.rect.y += self.dir.y * speed
        self.collision("v")

    def update(self):
        self.input()
        self.move(self.speed)
