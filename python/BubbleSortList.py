from List import List
import datetime

class BubbleSortList(List):
    def sort(self):
        self.start_time = datetime.datetime.now()
        self.bubble_sort()
        self.end_time = datetime.datetime.now()
        self.time_elapsed = self.end_time - self.start_time
        return self.time_elapsed
    
    def bubble_sort(self):
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
                    self.swap(j, j + 1)
                    
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