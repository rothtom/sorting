import os
# hides the hello message which is a side product of the screen init function of pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
import sys

from arg_manipulation import check_usage
from BogoSortList import BogoSortList
from BubbleSortList import BubbleSortList
from MergeSortList import MergeSortList
from QuickSortList import QuickSortList
from SelectionSortList import SelectionSortList

FPS = 60

stop = False

def main():
    pg.init()
    
    
    clock = pg.time.Clock()
    args = check_usage()
    pg.display.set_caption(f"Sorting ({args['algorithm'] + '-sort'})")
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
            list.draw(time=False)
            list.sort()
            list.time_to_seconds()
            print(f"Time overall:   {list.time_elapsed:.6f} seconds")
            print(f"Time drawing:   {list.time_drawing:.6f} seconds ({((list.time_drawing / list.time_elapsed) * 100):.3f}%)")
            print(f"Time paused:    {list.time_paused:.6f} seconds ({((list.time_paused / list.time_elapsed) * 100):.3f}%)")
            print(f"Time sorted:    {list.time_sorted:.6f} seconds ({((list.time_sorted / list.time_elapsed) * 100):.3f}%)")
            print(f"Swapped a total of {list.swaps} times.")
            
            list.reset_highlights()
            list.draw(time=False)





def initialize_list(args):
    match args["algorithm"]:
        case "bogo":
            return BogoSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_tuple"], delay=args["delay"], stop=args["stop"])
        case "bubble":
            return BubbleSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_tuple"], delay=args["delay"], stop=args["stop"])
        case "merge":
            return MergeSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_tuple"], delay=args["delay"], stop=args["stop"])
        case "quick":
            return QuickSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_tuple"], delay=args["delay"], stop=args["stop"])
        case "selection":
            return SelectionSortList(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_tuple=args["start_tuple"], delay=args["delay"], stop=args["stop"])
        case _:
            raise ValueError


def on_key_down(key):
    print(key)
    if key == pg.K_SPACE:
        global stop
        if stop:
            stop = False
        else:
            stop = True


if __name__ == "__main__":
    main()