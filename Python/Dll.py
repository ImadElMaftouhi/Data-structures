###########
#Double linked list


class DllNode:
    """
    Represents a node in a doubly linked list.
    """
    def __init__(self, data, next_node=None, prev_node=None):
        """
        Initializes a new node with the given data and optional next and previous nodes.
        """
        self.data = data
        self.next = next_node
        self.prev = prev_node

class Dll:
    """
    Represents a doubly linked list.
    """
    def __init__(self):
        """
        Initializes an empty doubly linked list.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def dll_prepend(self, data):
        """
        Inserts a new node with the given data at the beginning of the list.
        """
        new_node = DllNode(data, next_node=self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def dll_append(self, data):
        """
        Inserts a new node with the given data at the end of the list.
        """
        new_node = DllNode(data, prev_node=self.tail)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def dll_print(self):
        """
        Prints the data of each node in the list.
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next


#     """
#     uncomment the following main function to test function to demonstrate usage of the doubly linked list. Just make sure to to comment if you wish to run main.py or you will run into errors.
#     """
# def main():
#     dlist = Dll()
#     dlist.dll_append(1)
#     dlist.dll_append(2)
#     dlist.dll_append(3)

#     print("Doubly linked list:")
#     dlist.dll_print()

# if __name__ == "__main__":
#     main()
