import pygame
from csv import reader
from os import walk


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=",")
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    surface_list = []
    for _, _, img_files in walk(path):
        for img in img_files:
            full_path = path + "/" + img
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)
    return surface_list


def get_image(file, frame_x, frame_y, img_width, img_height, scale):
    img = pygame.Surface((img_width, img_height)).convert_alpha()
    img.blit(file, (0, 0), ((frame_x * img_width), (frame_y * img_height), img_width, img_height))
    img = pygame.transform.scale(img, (img_width * scale, img_height * scale))
    return img