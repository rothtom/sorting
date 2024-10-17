import pygame as pg
import argparse
# import sys
import datetime
import random

numbers = range(1, 100)
HEIGHT = 720
WIDTH = 1280
MAX_PILLAR_HEIGHT = int((HEIGHT - 20) / 100)
DEFAULT_LIST_LENGTH = 100
POSSIBLE_LAGORITHMS = ["bogo", "bogo-sort", ]
class Pillar():
    def __init__(self, value):
        self.value = value
        
class List():
    def __init__(self, algorithm, length=0, seed=1, start_list=None):
        # check validity of kwargs
        assert type(length) == int
        assert algorithm in POSSIBLE_LAGORITHMS
        
        # if you dont want a random list but rather a preconfigured one
        if start_list != None:
            self.pillars = []
            for value in start_list:
                self.pillars.append(Pillar(value=value))
        else:
            possible_numbers = list(range(1, length + 1))
            self.pillars = []
            
            # set random seed randomly by default, same seed possibke for same results
            random.seed(seed)
            for _ in range(length):
                # select a random number from the possible numbers left
                num = random.choice(possible_numbers)
                
                self.pillars.append(Pillar(value=num))
                
                # remove the just added number from the possible numbers so we dont have dubbles
                possible_numbers.remove(num)
    
    def check_sorted(self):
        for i in range(len(self.pillars) - 1):
            if self.pillars[i].value > self.pillars[i + 1].value:
                return False
        return True

def main():
    # check for valid usage
    args = check_usage()
    
    list = List(length=args["length"], seed=args["seed"], algorithm=args["algorithm"])
    
    # setup pygame
    pg.init()
    pg.display.set_mode((WIDTH, HEIGHT))


def check_usage():
    # check for right usage of command line arguments
    parser = argparse.ArgumentParser(
        prog="main.py",
            usage="python main.py --list_length {int} (deafult=100) --seed {float} (default=current timestamp)",
    )
    parser.add_argument("-l", "--length", default=DEFAULT_LIST_LENGTH, type=int)
    parser.add_argument("-s", "--seed", default=datetime.datetime.now().timestamp(), type=float)
    # for now not required and defaults to bogo
    parser.add_argument("-a", "--algorithm", 
                        #required=True,
                        # add more algorithms later
                        choices=POSSIBLE_LAGORITHMS,
                        default="bogo"
                        )
    # args is a dict of the key-value pairs from the command-line
    args = vars(parser.parse_args())
    return args

if __name__=="__main__":
    main()