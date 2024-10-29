import datetime
import time
import random
import pygame as pg

from Pillar import Pillar

DEFAULT_RANDOM_SEED = datetime.datetime.now().timestamp()
DEFAULT_LIST_LENGTH = 100
POSSIBLE_ALGORITHMS = ["bogo", "bubble", "selection", "merge"]

HEIGHT = 720
max_width = 1280

MAX_PILLAR_HEIGHT = int(HEIGHT * 0.9)
MARGIN = (HEIGHT - MAX_PILLAR_HEIGHT) / 2
PILLAR_PADDING_REL = 0.02


class List():
    # length ist hier optional, um besser mit bereits gegebenen Listen testen zu können.
    # wenn es eine liste zum starten gibt, ist die länge unnötig
    def __init__(self, algorithm, length=None, seed=DEFAULT_RANDOM_SEED, start_list=None, delay=0):
        """
        Creates a list of Pillars, randomly arranged, except if there is a start list of values - then it uses those.
        - start_list is an option for giving a prearranged list of values for the values of the pillars.
        - length is a required parameter when not giving a start_list that determins the length of the randomly arranged.
        - seed is an option for a random seed so everytime you run it you get a differently arranged list. the random seed is constructed by the current system time
        which ensures a different seed everytime you run it
        - algorithm determins which algorithm is used to sort the list after calling the sort method in it. It has to be one of the options of POSSIBLE_ALGORITHMS
        """
        
        # format the sorting algorythm into valid options
        self.algorithm = algorithm.split("-")[0]
        self.algorithm = self.algorithm.split("_")[0]
        
        # check validity of kwargs
        
        # check if the algorithm is possible
        assert self.algorithm in POSSIBLE_ALGORITHMS
        
        # check if the seed has the right datatype
        assert (type(seed) == int or type(seed) == float)
        
        self.algorithm = algorithm.replace("-sort", "")
        
        # if you dont want a random list but rather a preconfigured one
        if start_list != None:
            assert type(start_list) == tuple
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
                
        self.length = len(self.pillars)
        
        # the number of pixels a pillar is wide
        # must be an integer which causes problems
        global PILLAR_SPACE
        PILLAR_SPACE = int(max_width / self.length)
        
        # the ammount of pixels that are empty because of the rounding
        global width
        width = int((PILLAR_SPACE * self.length))

        # initalise screen with a dynamic width, so the pillars fit perfectly.
        # it wouldn't otherwise due to rounding impercision because pixels must be ints
        pg.init()
        self.screen = pg.display.set_mode((width, HEIGHT))
        
        assert type(delay) == float or type(delay) == int
        assert delay >= 0
        self.delay = delay
        
    def check_sorted(self):
        for i in range(len(self.pillars) - 1):
            if self.pillars[i].value > self.pillars[i + 1].value:
                return False
        return True
    
    def sort(self):
        if self.algorithm == "bogo":
            self.bogo_sort()
        elif self.algorithm == "selection":
            self.selection_sort()
        elif self.algorithm == "merge":
            self.merge_sort()
        elif self.algorithm == "bubble":
            self.bubble_sort()
        else:
            raise NotImplementedError
    
    def bogo_sort(self):
        pass
    
    def selection_sort(self):
        self.draw()
        for i in range(self.length - 1):
            smallest_index = i
            self.pillars[smallest_index].selected = True
            self.draw()
            
            for j in range(i + 1, self.length):
                self.pillars[j].comparing = True
                if self.pillars[smallest_index].value > self.pillars[j].value:
                    self.draw()
                    self.pillars[smallest_index].selected = False
                    smallest_index = j
                    self.pillars[smallest_index].comparing = False
                    self.pillars[smallest_index].selected = True
                self.draw()
                self.pillars[j].comparing = False
            
            # TODO
            # switch i-th and smallest_index pillar
            self.pillars[i].swapping = True
            self.draw()
            temp = self.pillars[i]
            self.pillars[i] = self.pillars[smallest_index]
            self.pillars[smallest_index] = temp
            self.draw()
            self.pillars[smallest_index].swapping = False
            self.pillars[i].selected = False

    def merge_sort(self):
        pass

    def bubble_sort(self, context=None):
        """
        Bubblesorts the list of Pillars in List.pillars
        Bubblesort compares a item to its right one and switches them if neccessarry. The next item becomes the one that compares its right neighbour to itself and so on...
        """
        # go through every item in the list for every item there is - so if the last one has to be at the front or the first one all the way in the back 
        # you have to switch that item a total of n - 1 times
        for i in range(self.length - 1):
            # draw everything wihtout any hioghlights to show new iteration
            self.draw()
            swapped = False
            # go through every item in the list and comapre it to its right neighbour
            for j in range(self.length - (i + 1)):
                # for visualisation important
                self.pillars[j].selected = True
                self.pillars[j + 1].comparing = True
                self.draw()
                
                # if the left one is smaller -> switch them
                if self.pillars[j].value > self.pillars[j + 1].value:
                    # indicate that those pillars get swapped for visualisation
                    self.pillars[j + 1].comparing = False
                    self.pillars[j + 1].swapping = True
                    # show swapping visually by drawing the list after swapping with the same highlighted Pillars
                    self.draw()
                    
                    # switches the two compared elements
                    ptemp = self.pillars[j]
                    self.pillars[j] = self.pillars[j + 1]
                    self.pillars[j + 1] = ptemp
                    
                    
                    self.draw()
                    # algorithm goes on until he gets through wihout switching something or after i iterations
                    swapped = True
                    
                    # reset the pillars visualisation status after swapping them
                    self.pillars[j + 1].selected = False
                    self.pillars[j].swapping = False
                
                else:
                    # reset the pillars visualisation status
                    self.pillars[j].selected = False
                    self.pillars[j + 1].comparing = False
            # if the algorithm didnt switch something its sorted. -> quits
            if swapped == False:
                break
            
    def draw(self):
        self.screen.fill("black")
        for i in range(self.length):
            
            pillar_height = int(MAX_PILLAR_HEIGHT * (self.pillars[i].value / self.length))
            pillar_width = int(PILLAR_SPACE - (PILLAR_SPACE * PILLAR_PADDING_REL))
            
            y = int(HEIGHT - (pillar_height))
            x = int((PILLAR_SPACE * i) + (PILLAR_SPACE * (PILLAR_PADDING_REL / 2)))
            self.pillars[i].draw_pillar(self.screen, x, y, pillar_width, pillar_height)
        pg.display.flip()
        time.sleep(self.delay)
            
    def __str__(self):
        string = f"len: {len(self.pillars)}\nsorted: {self.check_sorted()}\n"
        for i in range(len(self.pillars)):
            string = string + str(self.pillars[i].value) + " "
        string = string + "\n"
        return string