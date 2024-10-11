import pygame as pg
import sys
import random

numbers = range(1, 100)
HEIGHT = 720
WIDTH = 1280
MAX_PILLAR_HEIGHT = int((HEIGHT - 20) / 100)
class Pillar():
    def __init__(self, number):
        self.number = number
        self.height = MAX_PILLAR_HEIGHT * self.number

def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        sys.exit("usage: python main.py {list length} {seed}(optional)")
    try:
        global LIST_LENGTH = int(sys.argv[1])
    if sys.argv[1] < 2:
        sys.exit("list length must ber grater than two")
    if sys.argv[1] >= 1000:
        sys.exit("the maximum list length is 1000")
    # setup pygame
    pg.init()
    pg.display.set_mode((WIDTH, HEIGHT))
    

if __name__=="__main__":
    main()