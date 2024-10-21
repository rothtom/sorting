from tkinter import *

from main import List, Pillar
from arg_manipulation import check_usage

HEIGHT = 720
WIDTH = 1280
MAX_PILLAR_HEIGHT = int(HEIGHT * 0.8)
MARGIN = (HEIGHT - MAX_PILLAR_HEIGHT) / 2

class Visualizer():
    def __init__(self, list):
        self.list = list
        self.length = len(self.list.pillars)
        
    def draw(self):
        for i in range(len(self.list.pillars)):
            pillar_height = MAX_PILLAR_HEIGHT * (self.list.pillars[i].value / self.length)
            y_offset = MAX_PILLAR_HEIGHT - (pillar_height)
            

def main():
    args = check_usage()
    list = List(algorithm=args["algorithm"], length=args["length"], seed=args["seed"], start_list=args["start_list"])
    list.sort()
    print(list)

if __name__ == "__main__":
    main()