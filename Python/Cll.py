##########
##Circular simple linked list

import Sll as sll

class Cll():
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def cll_append(self, data):
        new_node = sll.SllNode(data)
        
        if not self.head:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not self.head and ptr.next is not None :
                ptr = ptr.next
            ptr.next = new_node
            new_node.next = self.head
        self.size += 1
        return new_node
                
    def cll_print(self, head) -> None:
        print("\n", head.data)
        if ( head.next is not self.head and head is not None ) :
            self.cll_print(head.next)
        