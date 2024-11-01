import pygame as pg


NORMAL_COLOR = "green"
SELECTED_COLOR = "red"
COMPARING_COLOR = "blue"
SWAPPING_COLOR = "purple"

class Pillar():
    def __init__(self, value):
        self.value = value
        self.comparing = False
        self.selected = False
        self.swapping = False
        self.hidden = False
        
    def draw_pillar(self, screen, x, y, width, height):
        rect = pg.Rect(x, y, width, height)
        if self.hidden:
            return 0
        elif self.swapping:
            pg.draw.rect(screen, SWAPPING_COLOR, rect)
        elif self.selected:
            pg.draw.rect(screen, SELECTED_COLOR, rect)
        elif self.comparing:
            pg.draw.rect(screen, COMPARING_COLOR, rect)
        else:
            pg.draw.rect(screen, NORMAL_COLOR, rect)

    def __str__(self):
        return f"{self.value}"