class MinHeap:
    """Custom implementation of a min heap (priority queue)"""

    def __init__(self):
        self.heap = []
        self.size = 0
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def has_parent(self, i):
        return self.parent(i) >= 0
    
    def has_left_child(self, i):
        return self.left_child(i) < self.size
    
    def has_right_child(self, i):
        return self.right_child(i) < self.size
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def peek(self):
        """Get the minimum element without removing it"""
        if self.size == 0:
            return None
        return self.heap[0]
    
    def push(self, item):
        """Add an item to the heap"""
        self.heap.append(item)
        self.size += 1
        self._heapify_up(self.size - 1)
    
    def pop(self):
        """Remove and return the minimum element"""
        if self.size == 0:
            return None
        
        item = self.heap[0]

        # Move the last item to the root and heapify down
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()

        if self.size > 0:
            self._heapify_down(0)
        
        return item
    
    def _heapify_up(self, index):
        """Restore heap property after insertion"""
        while (self.has_parent(index) and 
               self.heap[self.parent(index)] > self.heap[index]):
            parent_index = self.parent(index)
            self.swap(index, parent_index)
            index = parent_index
        
    def _heapify_down(self, index):
        """Restore heap property after removal"""
        smallest = index

        # Check if left child is smaller than current smallest
        if (self.has_left_child(index) and
            self.heap[self.left_child(index)] < self.heap[smallest]):
            smallest = self.left_child(index)
        
        # Check if right child is smaller than current smallest
        if (self.has_right_child(index) and
            self.heap[self.right_child(index)] < self.heap[smallest]):
            smallest = self.right_child(index)
        
        # if smallest is not the current index, swap and continue heapifying
        if smallest != index:
            self.swap(index, smallest)
            self._heapify_down(smallest)
        
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0