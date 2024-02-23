from Sll import SllNode

class Stack:
    """
    Represents a stack data structure implemented using a singly linked list.
    
    A stack follows the Last-In-First-Out (LIFO) principle, where the last element pushed onto the stack is the first to be popped off.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        """
        Pushes a new element onto the top of the stack.
        
        Args:
        - data: The data to be pushed onto the stack.
        
        Returns:
        - The newly created node representing the pushed element.
        """
        new_node = SllNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return new_node

    def pop(self):
        """
        Pops the top element from the stack.
        
        Returns:
        - The node representing the popped element, or None if the stack is empty.
        """
        if self.is_empty():
            return None
        ptr = self.head
        while ptr.next is not self.tail:
            ptr = ptr.next
        temp = self.tail
        self.tail = ptr
        self.tail.next = None
        self.size -= 1
        return temp

    def delete(self, index):
        """
        Deletes the element at the specified index in the stack.
        
        Args:
        - index: The index of the element to be deleted.
        
        Returns:
        - True if the element was successfully deleted, False otherwise.
        """
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            ptr = self.head
            for _ in range(index - 2):
                ptr = ptr.next
            ptr.next = ptr.next.next
        self.size -= 1
        return True

    def insert(self, data, index):
        """
        Inserts an element at the specified index in the stack.
        
        Args:
        - data: The data to be inserted.
        - index: The index at which to insert the element.
        
        Returns:
        - True if the element was successfully inserted, False otherwise.
        """
        if index < 0 or index > self.size:
            return False
        new_node = SllNode(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            ptr = self.head
            for _ in range(index - 1):
                ptr = ptr.next
            new_node.next = ptr.next
            ptr.next = new_node
        self.size += 1
        return True

    def stack_print(self):
        """
        Prints the elements of the stack from top to bottom.
        """
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def is_empty(self):
        """
        Checks if the stack is empty.
        
        Returns:
        - True if the stack is empty, False otherwise.
        """
        return self.size == 0
