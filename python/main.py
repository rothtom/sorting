import pygame as pg

from arg_manipulation import check_usage
from List import List, WIDTH, HEIGHT

def main():
    args = check_usage()
    list = List(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_list=args["start_list"], steps=args["steps"], delay=args["delay"])
    running = True
    sorting = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            pg.quit()
        if sorting:
            list.sort()
        if list.check_sorted():
            sorting = False
            
        
if __name__ == "__main__":
    main()