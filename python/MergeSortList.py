from List import List

class MergeSortList(List):
    def sort(self, left_index, right_index):
        for i in range(left_index, right_index + 1):
            self.pillars[i].selected = True
        self.draw()
        for i in range(left_index, right_index + 1):
            self.pillars[i].selected = False
                
        # the distance between the left and right index will grow smaller untill their both at the end, it will then return
        if left_index < right_index:
            middle = (left_index + right_index) // 2
            self.merge_sort(left_index, middle)
            
            self.merge_sort(middle + 1, right_index)
            
            self.merge(left_index, right_index , middle)


    def merge(self, left_index, right_index, middle):
        for i in range(left_index, right_index + 1):
            self.pillars[i].swapping = True
        self.draw()
        for i in range(left_index, right_index + 1):
            self.pillars[i].swapping = False
            self.pillars[i].hidden = True
        self.draw()
        
        length_left = middle - left_index + 1
        length_right = right_index - middle
        
        left_list = [None] * length_left
        for i in range(length_left):
            left_list[i] = self.pillars[left_index + i]
        
        right_list = [None] * length_right
        
        for i in range(length_right):
            right_list[i] = self.pillars[middle + 1 + i]

        i = j = 0
        k = left_index
        while i < length_left and j < length_right:
            if left_list[i].value < right_list[j].value:
                self.swap(k, self.find_pillar_index_by_value(left_list[i].value)[-1])
                i += 1
            else:
                self.swap(k, self.find_pillar_index_by_value(right_list[j].value)[-1])
                j += 1
            self.pillars[k].hidden = False
            k += 1
            self.draw()
            
        while i < length_left:
            self.swap(k, self.find_pillar_index_by_value(left_list[i].value)[-1])
            self.pillars[k].hidden = False
            self.draw()
            i += 1
            k += 1
        
        while j < length_right:
            self.swap(k, self.find_pillar_index_by_value(right_list[j].value)[-1])
            self.pillars[k].hidden = False
            self.draw()
            j += 1
            k += 1
            
        # in this case the comparing visualisation indicates completion of sorting
        for i in range(left_index, k):
            self.pillars[i].comparing = True
        self.draw()
        for i in range(left_index, k):
            self.pillars[i].comparing = False
        self.draw()