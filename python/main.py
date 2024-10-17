import pygame as pg
import sys
import datetime
import random

numbers = range(1, 100)
HEIGHT = 720
WIDTH = 1280
MAX_PILLAR_HEIGHT = int((HEIGHT - 20) / 100)
DEFAULT_LIST_LENGTH = 100
class Pillar():
    def __init__(self, number):
        self.number = number
        
class List():
    def __init__(self, length=DEFAULT_LIST_LENGTH, seed=datetime.datetime.now().timestamp()):
        # check validity of kwargs
        assert type(length) == int
        
        possible_numbers = list(range(length))
        self.pillars = []
        
        # set random seed randomly by default, same seed possibke for same results
        random.seed(seed)
        for _ in range(length):
            # select a random number from the possible numbers left
            num = random.choice(possible_numbers)
            
            self.pillars.append(Pillar(value=num))
            
            # remove the just added number from the possible numbers so we dont have dubbles
            possible_numbers.remove(num)

def main():
    # check for valid usage
    check_usage(sys.argv)
    
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