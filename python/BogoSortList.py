from List import List
import random
import datetime

class BogoSortList(List):
    def sort(self):
        self.start_time = datetime.datetime.now()
        self.bogo_sort()
        self.end_time = datetime.datetime.now()
        self.calculate_time()
        return self.time_elapsed
    def bogo_sort(self):
        while True:
            self.draw()
            random.shuffle(self.pillars)
            sorted = self.check_sorted()
            if sorted:
                break
        self.draw()