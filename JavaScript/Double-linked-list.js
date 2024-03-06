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