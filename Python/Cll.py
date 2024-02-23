##########
##Circular simple linked list
import Sll as sll

class Cll:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def cll_append(self, data):
        new_node = sll.SllNode(data)
        
        if not self.head:
            self.head = new_node
            new_node.next = new_node  # Make it circular
        else:
            ptr = self.head
            while ptr.next is not self.head:
                ptr = ptr.next
            ptr.next = new_node
            new_node.next = self.head
        self.size += 1
        return new_node
                
    def cll_print(self):
        if not self.head:
            print("Circular linked list is empty")
            return
        
        ptr = self.head
        while True:
            print(ptr.data)
            ptr = ptr.next
            if ptr is self.head:
                break

# def main():
#     cllist = Cll()
#     cllist.cll_append(1)
#     cllist.cll_append(2)
#     cllist.cll_append(3)

#     print("Circular linked list:")
#     cllist.cll_print()

# if __name__ == "__main__":
#     main()
