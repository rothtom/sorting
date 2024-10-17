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
POSSIBLE_LAGORITHMS = ["bogo", "bogo-sort", "bubble", "bubble_sort", ]

class Pillar():
    def __init__(self, value):
        self.value = value
        self.comparing = False
        self.selected = False
        
class List():
    def __init__(self, algorithm, length=None, seed=datetime.datetime.now().timestamp(), start_list=None):
        """
        Creates a list of Pillars, randomly arranged, except if there is a start list of values - then it uses those.
        - start_list is an option for giving a prearranged list of values for the values of the pillars.
        - length is a required parameter when not giving a start_list that determins the length of the randomly arranged.
        - seed is an option for a random seed so everytime you run it you get a differently arranged list. the random seed is constructed by the current system time
        which ensures a different seed everytime you run it
        - algorithm determins which algorithm is used to sort the list after calling the sort method in it. It has to be one of the options of POSSIBLE_ALGORITHMS
        """
        # check validity of kwargs
        
        assert algorithm in POSSIBLE_LAGORITHMS
        assert (type(seed) == int or type(seed) == float)
        
        self.algorithm = algorithm.replace("-sort", "")
        
        # if you dont want a random list but rather a preconfigured one
        if start_list != None:
            self.pillars = []
            for value in start_list:
                self.pillars.append(Pillar(value=value))
        else:
            # check for valid length is a valid integer grater than 0
            assert length != None
            assert type(length) == int
            assert length > 0
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
    
    def sort(self):
        if self.algorithm == "bogo":
            self.bogo_sort()
        elif self.algorithm == "merge":
            self.merge_sort()
        elif self.algorithm == "bubble":
            self.bubble_sort()
    
    def bogo_sort(self):
        pass
    
    def selection_sort(self):
        pass

    def merge_sort(self):
        pass

    def bubble_sort(self):
        """
        Bubblesorts the list of Pillars in List.pillars
        Bubblesort compares a item to its right one and switches them if neccessarry. The next item becomes the one that compares its right neighbour to itself and so on...
        """
        # go through every item in the list for every item there is - so if the last one has to be at the front or the first one all the way in the back 
        # you have to switch that item a total of n - 1 times
        for i in range(len(self.pillars)):
            swapped = False
            
            # go through every item in the list and comapre it to its right neighbour
            for j in range( len(self.pillars) - 1):
                
                # inefficient but makes programming easier, those are the i-th and i+1-th Pillars from the pillarlist in List
                p1 = self.pillars[j]
                p2 = self.pillars[j + 1]
                # for visualisation important
                p1.selected = True
                p2.comparing = True
                # if the left one is smaller -> switch them
                if self.pillars[i].value > self.pillars[i + 1].value:
                    # algorythm goes on until he gets through wihout switching something
                    swapped = True
                    # switches the two comapred elements
                    p1, p2 = p2, p1
                # for visualisation important
                p1.selected = False
                p2.comparing = False
            if swapped == False:
                break
    def __str__(self):
        string = f"len: {len(self.pillars)}\nsorted: {self.check_sorted()}\n"
        for i in range(len(self.pillars)):
            string = string + str(self.pillars[i].value)
        string = string + "\n"
        print(string)
        return string

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