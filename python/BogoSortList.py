from List import List
import random

class BogoSortList(List):
    def sort(self):
        while True:
            self.draw()
            random.shuffle(self.pillars)
            sorted = self.check_sorted()
            if sorted:
                break
        self.draw()