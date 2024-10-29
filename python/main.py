import pygame as pg

from arg_manipulation import check_usage
from List import List

def main():
    args = check_usage()
    list = List(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_list"], delay=args["delay"])
    running = True
    sorting = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            pg.quit()

        list.sort()
        running = False

if __name__ == "__main__":
    main()