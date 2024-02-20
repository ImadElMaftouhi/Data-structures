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

    