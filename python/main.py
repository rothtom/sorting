import pygame as pg
import sys
import random

numbers = range(1, 100)
HEIGHT = 720
WIDTH = 1280
MAX_PILLAR_HEIGHT = int((HEIGHT - 20) / 100)
DEFAULT_LIST_LENGTH = 100
class Pillar():
    def __init__(self, number):
        self.number = number
        self.height = MAX_PILLAR_HEIGHT * self.number

def main():
    # check for valid usage
    check_usage(sys.argv)
    
    unsorted = 
    possible_numbers_list = list(range(list_length))
    for i in range(list_length):
        unsorted[i] = possible_numbers_list.remove(random.choice(possible_numbers_list))
    
    print(unsorted)
    # setup pygame
    pg.init()
    pg.display.set_mode((WIDTH, HEIGHT))


def check_usage(args):
    # check for right number of command line arguments
    if len(args) < 1 or len(args) > 3:
        sys.exit("usage: python main.py {list length}(optional, default=100) {seed}(optional)")
    try:
        global list_length
        list_length = int(args[1])
    
    # if not list length is given -> use default
    except IndexError:
        list_length = DEFAULT_LIST_LENGTH
    # if the list length isnt a int -> exit
    except TypeError:
        sys.exit("list length must be an integer")
        
    if list_length < 2:
        sys.exit("list length must ber grater than two")
        
    if list_length >= 1000:
        sys.exit("the maximum list length is 1000")
    print(f"List length: {list_length}")

if __name__=="__main__":
    main()