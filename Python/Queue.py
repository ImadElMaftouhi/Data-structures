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
        return new_node
    
    def pop(self):
        ptr = self.head
        self.head = self.head.next # Moving the head to the next node in the list
        return ptr # Returning the data, the order of this function is necessary.
    

    