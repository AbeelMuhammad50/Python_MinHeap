# Lab #9
# Due Date: 11/08/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#  
########################################


class MinHeap:
    """
        >>> h = MinHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h.heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.parent(2)
        2
        >>> h.leftChild(1)
        5
        >>> h.rightChild(1)
        11
        >>> h.parent(8)
        10
        >>> h.leftChild(6)
        >>> h.rightChild(9)
        >>> h.deleteMin
        2
        >>> h.heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
    """

    # -- YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR!
    def __init__(self):
        self.heap = []

    def __str__(self):
        return f'{self.heap}'

    __repr__ = __str__

    # returns the value of the parent of heap[index]
    def parent(self, index):
        if index <= 1 or index > len(self):
            return None
        return self.heap[(index - 1) // 2]

    # returns the value of the left child of heap[index]
    def leftChild(self, index):
        if index < 1 or index > len(self):
            return None
        ind = 2 * (index - 1) + 1
        if ind > len(self) - 1:
            return  None
        return self.heap[ind]

    # returns the value of the right child of heap[index]
    def rightChild(self, index):
        if index < 1 or index > len(self):
            return None
        ind = 2 * (index - 1) + 2
        if ind > len(self) - 1:
            return None
        return self.heap[ind]

    # returns the number of items in the heap
    def __len__(self):
        return len(self.heap)

    # function is used in inserting a value to heap
    def push_upward(self,index):
        #check for upper bound 0
        if index > 0:
            # determines parent
            par = (index - 1) // 2
            # if current element is < it's parent
            if self.heap[index] < self.heap[par]:
                #swaps parent with child
                self.heap[index], self.heap[par] = self.heap[par], self.heap[index]
                self.push_upward(par)
        return

    # adds the item into the heap satisfying the min heap property
    def insert(self, x):
        self.heap.append(x)
        self.push_upward(len(self) - 1)

    # function assists deleteMin() function
    def push_downward(self, index):
        if index <  len(self):
            left, right = 2 * index + 1 , 2 * index + 2
            #validates if left index is in range
            if left < len(self):
                minimum = left
                if self.heap[right] < self.heap[minimum]:
                    minimum = right
                #swap the parent with min child of itself
                self.heap[minimum] , self.heap[index] = self.heap[index] , self.heap[minimum]
                #calls function again with min index
                self.push_downward(minimum)
        return

    # removes the min element of the heap (the root node).
    # The heap satisfies the min heap property after deletion.
    @property
    def deleteMin(self):
        if len(self) == 0:
            return None
        elif len(self) == 1:
            out = self.heap[0]
            self.heap = []
            return out
        else:
            #element to remove
            out = self.heap[0]
            #places last element at top
            self.heap[0] = self.heap[-1]
            #removes last element
            self.heap = self.heap[:-1]
            #calls helping function from index 0
            self.push_downward(0)
            return  out