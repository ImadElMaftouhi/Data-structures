########
#Simpled linked list 

class SllNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Sll:
    def __init__(self):
        self.head = None
        self.size = 0

    def sll_append(self, data):
        new_node = SllNode(data)
        if not self.head:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node
        self.size += 1

    def sll_prepend(self, data):
        new_node = SllNode(data, next_node=self.head)
        self.head = new_node
        self.size += 1

    def sll_print(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def sll_delete(self, index):
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            ptr = self.head
            for _ in range(index - 1):
                ptr = ptr.next
            ptr.next = ptr.next.next
        self.size -= 1
        return True

