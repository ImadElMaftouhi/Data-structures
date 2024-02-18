###########
#Double linked list


class DllNode:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class Dll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def dll_prepend(self, data):
        new_node = DllNode(data, next_node=self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def dll_append(self, data):
        new_node = DllNode(data, prev_node=self.tail)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def dll_print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

