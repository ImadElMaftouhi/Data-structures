## class queue and the functions associated

import Sll as sll

# A queue is a data structure where the first item in the list is the first item to exit/pop
# We say that a queue respect the FIFO principal.
# Meaning we insert new data at the end of the line and read from the firsts
class Queue():
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data) -> sll.SllNode:
        new_node = sll.SllNode(data)
        if self.head is None:
            self.head = new_node
        else :
            ptr = self.head
            while ( ptr.next is not None):
                ptr = ptr.next
            ptr.next = new_node
        self.size+=1 # Updating list size
        return new_node
    
    def pop(self):
        ptr = self.head
        self.head = self.head.next # Moving the head to the next node in the list
        return ptr # Returning the data, the order of this function is necessary.
    

    def delete(self, index) -> bool:
        if index < 0 or index > self.size:
            return False
        
        ptr = self.head
        
        for _ in range(index-2): # Iterating over the list i-1 time, we must stop before reaching our node's index.
            ptr = ptr.next

        ptr.next = ptr.next.next
        return True   

    def insert(self, index, data):
        if index < 0 or index > self.size:
            return False
        
        ptr = self.head
        new_node = sll.SllNode(data)

        for _ in range(index-2):
            ptr = ptr.next
        new_node.next = ptr.next
        ptr.next = new_node
        return True

    def peek(self):
        """Returns the element at the front of the queue without removing it."""
        if self.head is None:
            return None
        return self.head.data
    
    def is_empty(self):
        return self.size == 0
    
    def get(self, index):
        """Returns the element at the specified index without removing it."""
        if index < 0 or index >= self.size:
            return None
        
        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
        return ptr.data
    
    def contain(self, element):
        """Checks if the queue contains a specific element."""
        ptr = self.head
        while ptr:
            if ptr.data == element:
                return True
            ptr = ptr.next
        return False
    
    def index(self, element):
        """Returns the index of the first occurrence of the specified element in the queue."""
        ptr = self.head
        index = 0
        while ptr:
            if ptr.data == element:
                return index
            ptr = ptr.next
            index += 1
        return -1
    
    def extend(self, iterable):
        """Adds all elements from an iterable to the end of the queue."""
        for element in iterable:
            self.push(element)