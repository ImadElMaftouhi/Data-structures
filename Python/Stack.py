# Defining Class Stack and it's method


from Sll import SllNode

class SllNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


"""Stack
A Stack is a data structure that is built on one important principal, that is the first element inserted in the list should be the last item to process/read, we call this FILO principal.
In this library, the stacks is built on top of the simple linked list, where each node is linked to the next.
We have also defined a head to represent the first element, aswell as a 'tail' to represent the last item inserted in the list, thus making the insertion and deletion of nodes really simple and fast
"""
class Stack():
    
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def push(self, data, next_node = None) :
        new_node = SllNode(data, next_node)
       
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1 
        return new_node
    
    def pop(self):
        if self.head is None or self.tail is None :
            return None
        else:
            ptr = self.head
            while ptr.next is not self.tail:
                ptr = ptr.next
            temp = self.tail # storing the last node to be able to return and not lose any data
            self.tail = ptr
            self.tail.next = None
        self.size -= 1
        return temp
    
    def delete(self, index) -> bool:
        if self.head is None or self.tail is None :
            return False
        
        ptr = self.head
        
        for _ in range(index-2):
            ptr = ptr.next
        
        ptr.next = ptr.next.next 

        return True
    
    def insert(self, data, index) :
        
        if index > self.size or index < 0 :
            return False
        
        new_node = SllNode(data)
        ptr = self.head

        for _ in range(index-2):
            ptr = ptr.next
        
        new_node.next = ptr.next.next
        ptr.next = new_node

        self.size += 1

    def stack_print(self, head):
        if head is None:
            return 
        self.stack_print(head.next)
        print(head.data)
    
    