import os
# hides the hello message which is a side product of the screen init function of pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
import sys

import time

from arg_manipulation import check_usage
from BogoSortList import BogoSortList
from BubbleSortList import BubbleSortList
from MergeSortList import MergeSortList
from QuickSortList import QuickSortList
from SelectionSortList import SelectionSortList

FPS = 60



def main():
    pg.init()
    
    clock = pg.time.Clock()
    args = check_usage()
    list = initialize_list(args)
    
    
    
    
    running = True
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            sys.exit()

        if not list.check_sorted(visualize=False):
            list.sort()
            print(f"Time overall:   {list.time_elapsed} seconds")
            print(f"Time waited:    {list.time_waited} seconds")
            print(f"Time sorted:    {list.time_sorted} seconds")
            
            
            list.reset_highlights()
            list.draw()





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