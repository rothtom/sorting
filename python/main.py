import pygame as pg

from arg_manipulation import check_usage
from BogoSortList import BogoSortList
from BubbleSortList import BubbleSortList
from MergeSortList import MergeSortList
from QuickSortList import QuickSortList
from SelectionSortList import SelectionSortList

def main():
    args = check_usage()
    list = initialize_list(args)
    list.sort()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            pg.quit()

        duration = list.sort()
        print(duration)
        running = False
        
def initialize_list(args):
    if args["algorithm"] == "bogo":
        return BogoSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_list"], delay=args["delay"])
    if args["algorithm"] == "bubble":
        return BubbleSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_list"], delay=args["delay"])
    if args["algorithm"] == "merge":
        return MergeSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_list"], delay=args["delay"])
    if args["algorithm"] == "quick":
        return QuickSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_list"], delay=args["delay"])
    if args["algorithm"] == "selection":
        return SelectionSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_list"], delay=args["delay"])
    raise ValueError

if __name__ == "__main__":
    main()