import pygame as pg

class Pillar():
    def __init__(self, value):
        self.value = value
        self.comparing = False
        self.selected = False
        
    def draw_pillar(self, screen, x, y, width, height):
        rect = pg.Rect(x, y, width, height)
        if self.comparing:
            pg.draw.rect(screen, "blue", rect)
        elif self.selected:
            pg.draw.rect(screen, "red", rect)
        else:
            pg.draw.rect(screen, "green", rect)