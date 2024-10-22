import pygame as pg

from arg_manipulation import check_usage
from List import List, WIDTH, HEIGHT

def main():
    args = check_usage()
    list = List(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_list=args["start_list"])
    pg.init()
    print(WIDTH, HEIGHT)
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        list.draw(screen=screen)
    
if __name__ == "__main__":
    main()