import datetime
import time
import random
import sys

import pygame as pg

from Pillar import Pillar

DEFAULT_RANDOM_SEED = datetime.datetime.now().timestamp()
DEFAULT_LIST_LENGTH = 100
POSSIBLE_ALGORITHMS = ["bogo", "bubble", "selection", "merge", "quick"]

HEIGHT = 720
MAX_WIDTH = 1280

MAX_PILLAR_HEIGHT = int(HEIGHT - 60 - 32 - 15)
MARGIN = (HEIGHT - MAX_PILLAR_HEIGHT) / 2
PILLAR_PADDING_REL = 0.02

pg.font.init()
font1 = pg.font.Font(open("fonts/Audiowide-Regular.ttf", "r"), 48)
font2 = pg.font.Font(open("fonts/Audiowide-Regular.ttf", "r"), 32)

class List():
    # length ist hier optional, um besser mit bereits gegebenen Listen testen zu können.
    # wenn es eine liste zum starten gibt, ist die länge unnötig
    def __init__(self, algorithm, length=None, seed=DEFAULT_RANDOM_SEED, start_tuple=None, delay=0, stop=False):
        """
        Creates a list of Pillars, randomly arranged, except if there is a start list of values - then it uses those.
        - start_tuple is an option for giving a prearranged list of values for the values of the pillars.
        - length is a required parameter when not giving a start_tuple that determins the length of the randomly arranged.
        - seed is an option for a random seed so everytime you run it you get a differently arranged list. the random seed is constructed by the current system time
        which ensures a different seed everytime you run it
        - algorithm keeps track of which algorythm is used
        - stop desides wether the algorithm waits for the user to start sorting
        """
        
        
        # kwargs validitys are checked before tring to instantiate the object
        
        # check if the seed has the right datatype
        assert (type(seed) == int or type(seed) == float)
        self.seed = seed
        
        # if you dont want a random list but rather a preconfigured one
        if start_tuple != None:
            assert type(start_tuple) == tuple
            self.pillars = []
            for value in start_tuple:
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
        # must be an integer!
        global PILLAR_SPACE
        PILLAR_SPACE = int(MAX_WIDTH / self.length)
        
        # the ammount of pixels that are empty because of the rounding
        global WIDTH
        WIDTH = int((PILLAR_SPACE * self.length))

        # initalise screen with a dynamic width, so the pillars fit perfectly.
        # it wouldn't otherwise due to rounding impercision because pixels must be ints
        
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        
        assert type(delay) == float or type(delay) == int
        assert delay >= 0
        self.delay = delay

        self.algorithm = algorithm
        
        self.swaps = 0
        
        self.time_elapsed = datetime.timedelta(0,0)
        self.time_drawing = datetime.timedelta(0,0)
        self.time_sorted = datetime.timedelta(0,0)
        self.time_paused = datetime.timedelta(0,0)
        
        
        self.img1 = font1.render(self.algorithm.upper() + "-SORT", True, "green")
        self.img1_x = (WIDTH // 2) - (self.img1.get_width() // 2)
        
        self.stop = stop
        
        
    def check_sorted(self, visualize=True):
        for i in range(len(self.pillars) - 1):
            if visualize:
                self.pillars[i].selected = True
                self.pillars[i + 1].comparing = True
                self.draw()
                self.pillars[i].selected = False
                self.pillars[i + 1].comparing = False
            if self.pillars[i].value > self.pillars[i + 1].value:
                return False
        return True

    def find_pillar_index_by_value(self, value) -> list:
        """
        returns a list of indexes where the pillar has the targeted value
        """
        assert type(value) == int
        indexes = []
        for i in range(len(self.pillars)):
            if self.pillars[i].value == value:
                indexes.append(i)
        if len(indexes) > 0:
            return indexes
        raise ValueError
    
    def swap(self, index1, index2) -> None:
        """
        swaps the pillars of self.list in the index1-st and indext2-th place
        """
        temp = self.pillars[index1]
        self.pillars[index1] = self.pillars[index2]
        self.pillars[index2] = temp
        self.swaps += 1
        
    def draw(self, time=True):
        draw_start = datetime.datetime.now()
        self.screen.fill("black")
        for i in range(self.length):
            
            pillar_height = int(MAX_PILLAR_HEIGHT * (self.pillars[i].value / self.length))
            pillar_width = int(PILLAR_SPACE - (PILLAR_SPACE * PILLAR_PADDING_REL))
            
            y = int(HEIGHT - (pillar_height))
            x = int((PILLAR_SPACE * i) + (PILLAR_SPACE * (PILLAR_PADDING_REL / 2)))
            self.pillars[i].draw_pillar(self.screen, x, y, pillar_width, pillar_height)
            
        self.screen.blit(self.img1, (self.img1_x, 0))
        
        # dispaly time after finishing
        if self.time_sorted and type(self.time_sorted) != datetime.timedelta:
            self.img2 = font2.render(f"Time spent sorting: {self.time_sorted:.6f} seconds", True, "green")
            self.img2_x = (WIDTH // 2) - (self.img2.get_width() // 2)
            self.screen.blit(self.img2, (self.img2_x, 60))
            
        pg.display.flip()
        before_wait = datetime.datetime.now()
        waited_this_iteration = datetime.timedelta(0,0)
        while True:
            pg.event.pump()
            check_end()
            if pg.key.get_pressed()[pg.K_SPACE] or self.stop:
                waited_this_iteration += self.pause()
                if self.stop:
                    break
            if ((datetime.datetime.now() - before_wait) - waited_this_iteration).total_seconds() > self.delay:
                break

        if time:
            draw_end = datetime.datetime.now()
            draw_time = (draw_end - draw_start) - waited_this_iteration
            self.time_drawing += datetime.timedelta(0, draw_time.total_seconds())

    def pause(self):
        start_time = datetime.datetime.now()
        while True:
            pg.event.pump()
            check_end()
            if (datetime.datetime.now() - start_time).total_seconds() > 0.1:
                if pg.key.get_pressed()[pg.K_SPACE]:
                    self.stop = False
                    break
                if pg.key.get_pressed()[pg.K_RIGHT]:
                    self.stop = True
                    break
        time.sleep(0.1)
        paused = datetime.timedelta(0, (datetime.datetime.now() - start_time).total_seconds())
        self.time_paused += paused
        return paused
        
    def calculate_time(self) -> None:
        self.time_elapsed = self.end_time - self.start_time
        self.time_sorted = self.time_elapsed - self.time_drawing - self.time_paused
        
    def time_to_seconds(self):
        self.time_elapsed = self.time_elapsed.total_seconds()
        self.time_sorted = self.time_sorted.total_seconds()
        self.time_drawing = self.time_drawing.total_seconds()
        self.time_paused = self.time_paused.total_seconds()

    def reset_highlights(self) -> None:
        for pillar in self.pillars:
            pillar.comparing = False
            pillar.selected = False
            pillar.swapping = False
            pillar.hidden = False

    def __str__(self) -> str:
        string = f"len: {len(self.pillars)}\nsorted: {self.check_sorted()}\n"
        for i in range(len(self.pillars)):
            string = string + str(self.pillars[i].value) + " "
        string = string + "\n"
        return string

def check_end():
    if pg.key.get_pressed()[pg.K_ESCAPE]:
        sys.exit()