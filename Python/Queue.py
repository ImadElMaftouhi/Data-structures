## class queue and the functions associated

import Sll as sll

class Queue:
    """
    A queue data structure that follows the FIFO (First In, First Out) principle.
    """

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.head = None
        self.size = 0

    def push(self, data):
        """
        Adds an element to the end of the queue.
        
        Args:
        - data: The element to be added.
        """
        new_node = sll.SllNode(data)
        if self.head is None:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node
        self.size += 1

    def pop(self):
        """
        Removes and returns the element at the front of the queue.
        
        Returns:
        - The element at the front of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        ptr = self.head
        self.head = self.head.next
        self.size -= 1
        return ptr.data

    def delete(self, index):
        """
        Deletes the element at the specified index in the queue.
        
        Args:
        - index: The index of the element to be deleted.
        
        Returns:
        - True if the element was successfully deleted, False otherwise.
        """
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        ptr = self.head
        for _ in range(index - 1):
            ptr = ptr.next
        ptr.next = ptr.next.next
        self.size -= 1
        return True

    def insert(self, index, data):
        """
        Inserts an element at the specified index in the queue.
        
        Args:
        - index: The index at which to insert the element.
        - data: The element to be inserted.
        
        Returns:
        - True if the element was successfully inserted, False otherwise.
        """
        if index < 0 or index > self.size:
            return False
        new_node = sll.SllNode(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
        ptr = self.head
        for _ in range(index - 1):
            ptr = ptr.next
        new_node.next = ptr.next
        ptr.next = new_node
        self.size += 1
        return True

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.
        
        Returns:
        - The element at the front of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        """
        Checks if the queue is empty.
        
        Returns:
        - True if the queue is empty, False otherwise.
        """
        return self.size == 0

    def contain(self, element):
        """
        Checks if the queue contains a specific element.
        
        Args:
        - element: The element to check for.
        
        Returns:
        - True if the queue contains the element, False otherwise.
        """
        ptr = self.head
        while ptr:
            if ptr.data == element:
                return True
            ptr = ptr.next
        return False

    def index(self, element):
        """
        Returns the index of the first occurrence of the specified element in the queue.
        
        Args:
        - element: The element to search for.
        
        Returns:
        - The index of the element, or -1 if the element is not found.
        """
        ptr = self.head
        index = 0
        while ptr:
            if ptr.data == element:
                return index
            ptr = ptr.next
            index += 1
        return -1

    def extend(self, iterable):
        """
        Extends the queue by adding all elements from an iterable to the end of the queue.
        
        Args:
        - iterable: An iterable containing elements to be added to the queue.
        """
        for element in iterable:
            self.push(element)

    def reverse(self):
        """
        Reverses the order of elements in the queue.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def copy(self):
        """
        Creates a shallow copy of the queue.
        
        Returns:
        - A new queue containing the same elements as the original queue.
        """
        new_queue = Queue()
        ptr = self.head
        while ptr:
            new_queue.push(ptr.data)
            ptr = ptr.next
        return new_queue
