import os
# hides the hello message which is a side product of the screen init function of pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
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
    match args["algorithm"]:
        case "bogo":
            return BogoSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_tuple"], delay=args["delay"])
        case "bubble":
            return BubbleSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_tuple"], delay=args["delay"])
        case "merge":
            return MergeSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_tuple"], delay=args["delay"])
        case "quick":
            return QuickSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_tuple"], delay=args["delay"])
        case "selection":
            return SelectionSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_tuple"], delay=args["delay"])
        case _:
            raise ValueError

if __name__ == "__main__":
    main()