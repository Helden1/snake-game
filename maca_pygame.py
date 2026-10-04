import pygame
import random

def spawn_maca(number_lines, number_coluns, block_size):

    line = random.randint(1, number_lines-1)
    colunm = random.randint(1, number_coluns-1)
    vector_maca_pos = pygame.Vector2(line*block_size, colunm*block_size)
    return vector_maca_pos
