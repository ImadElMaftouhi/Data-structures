# Defining Class Stack and it's method


from Sll import SllNode

class SllNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node



class STack():
    
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
            return temp
    
    