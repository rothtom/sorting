from List import List

class QuickSortList(List):
    def quick_sort(self, left_index, right_index):
        # base case for recursion
        if left_index < right_index:
            pivot = self.partition(left_index, right_index)
            
            self.quick_sort(left_index, pivot - 1)

            self.quick_sort(pivot + 1, right_index)
            
    def partition(self, left_index, right_index):
        pivot = self.pillars[right_index]
        pivot.selected = True
        i = left_index - 1
        for j in range(left_index, right_index):
            self.pillars[j].selected = True
        self.draw()
        for j in range(left_index, right_index):
            self.pillars[j].selected = False
        
        for j in range(left_index, right_index):
            self.pillars[j].comparing = True
            self.draw()
            if self.pillars[j].value < pivot.value:
                i += 1
                # only swap if i and j are not the same, because it would then switch with itself
                if i != j:
                    self.pillars[i].swapping = True
                    self.pillars[j].swapping = True
                    self.draw()
                    self.swap(i, j)
                    self.draw()
                    self.pillars[i].swapping = False
                    self.pillars[j].swapping = False
                self.pillars[i].comparing = False
            else:
                self.pillars[j].comparing = False
        self.pillars[i + 1].swapping = True
        pivot.swapping = True
        self.draw()
        self.swap(i + 1, right_index)
        self.draw()
        self.pillars[right_index].swapping = False
        pivot.swapping = False
        pivot.selected = False
        return i + 1
    