import pygame as pg

from arg_manipulation import check_usage
from List import List, WIDTH, HEIGHT

def main():
    args = check_usage()
    pg.init()
    list = List(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_list=args["start_list"])
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            running = False
        list.screen.fill("black")
        list.sort()
        pg.display.flip()
    
if __name__ == "__main__":
    main()