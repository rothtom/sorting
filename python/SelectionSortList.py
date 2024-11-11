from List import List

class SelectionSortList(List):
    def sort(self):
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
            
            
            # switch i-th and smallest_index pillar and  visualise it
            self.pillars[i].swapping = True
            self.draw()
            self.swap(i, smallest_index)
            self.draw()
            self.pillars[smallest_index].swapping = False
            self.pillars[i].selected = False

