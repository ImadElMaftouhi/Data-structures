class Node {
    constructor(element) {
      this.element = element;
      this.next = null;
      this.prev = null;
    }
}

class DoublyLinkedList {
    constructor() {
      this.head = null;
      this.tail = null;
      this.size = 0;
    }

    add(element) {
        const newNode = new Node(element);
    
        if (this.head === null) {
          this.head = newNode;
          this.tail = newNode;
        } else {
          this.tail.next = newNode;
          newNode.prev = this.tail;
          this.tail = newNode;
        }
        this.size++;
    }

    insertAt(element, index) {
    if (index < 0 || index > this.size) {
        return false;
    } else {
        const newNode = new Node(element);
        let current, previous;
        current = this.head;
        if (index === 0) {
        newNode.next = this.head;
        this.head.prev = newNode;
        this.head = newNode;
        } else {
        let i = 0;
        while (i < index) {
            i++;
            previous = current;
            current = current.next;
        }
        newNode.next = current;
        newNode.prev = previous;
        current.prev = newNode;
        previous.next = newNode;
        }
        this.size++;
        return true;
    }
    }