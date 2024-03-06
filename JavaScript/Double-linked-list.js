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

    removeFrom(index) {
        if (index < 0 || index >= this.size) {
          return null;
        } else {
          let current, previous;
          current = this.head;
          if (index === 0) {
            this.head = current.next;
            if (this.head === null) {
              this.tail = null;
            } else {
              this.head.prev = null;
            }
          } else if (index === this.size - 1) {
            current = this.tail;
            this.tail = current.prev;
            this.tail.next = null;
          } else {
            let i = 0;
            while (i < index) {
              i++;
              previous = current;
              current = current.next;
            }
            previous.next = current.next;
            current.next.prev = previous;
          }
          this.size--;
          return current.element;
        }
    }

    removeElement(element) {
        let current = this.head;
        while (current !== null) {
          if (current.element === element) {
            if (current === this.head) {
              this.head = current.next;
              if (this.head === null) {
                this.tail = null;
              } else {
                this.head.prev = null;
              }
            } else if (current === this.tail) {
              this.tail = current.prev;
              this.tail.next = null;
            } else {
              current.prev.next = current.next;
              current.next.prev = current.prev;
            }
            this.size--;
            return current.element;
          }
          current = current.next;
        }
        return null;
      }
    
      indexOf(element) {
        let count = 0;
        let current = this.head;
        while (current !== null) {
          if (current.element === element) {
            return count;
          }
          count++;
          current = current.next;
        }
        return -1;
      }
    
      isEmpty() {
        return this.size === 0;
      }
    
      size_of_list() {
        return this.size;
      }
    
      printList() {
        let current = this.head;
        let str = "";
        while (current !== null) {
          str += current.element + " ";
          current = current.next;
        }
        console.log(str);
      }
    }