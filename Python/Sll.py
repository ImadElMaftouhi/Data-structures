########
#Simpled linked list 

class SllNode:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new node with the given data and optional next node.
        
        Args:
        - data: The data to be stored in the node.
        - next_node: Reference to the next node in the list. Defaults to None.
        """
        self.data = data
        self.next = next_node

class Sll:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None
        self.size = 0

    def sll_append(self, data):
        """
        Appends a new node with the given data to the end of the list.
        
        Args:
        - data: The data to be appended.
        """
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
        """
        Prepends a new node with the given data to the beginning of the list.
        
        Args:
        - data: The data to be prepended.
        """
        new_node = SllNode(data, next_node=self.head)
        self.head = new_node
        self.size += 1

    def sll_print(self):
        """
        Prints the data of each node in the list.
        """
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def sll_delete(self, index):
        """
        Deletes the node at the specified index in the list.
        
        Args:
        - index: The index of the node to be deleted.
        
        Returns:
        - True if the node was successfully deleted, False otherwise.
        """
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
