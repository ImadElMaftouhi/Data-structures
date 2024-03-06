class Node {
    constructor(element) {
      this.element = element;
      this.next = null;
    }
  }
  
  class LinkedList {
    constructor() {
      this.head = null;
      this.size = 0;
    }
  
    add(element) {
      const newNode = new Node(element);
      let current;
  
      if (this.head === null) {
        this.head = newNode;
      } else {
        current = this.head;
        while (current.next) {
          current = current.next;
        }
        current.next = newNode;
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
          this.head = newNode;
        } else {
          current = this.head;
          let i = 0;
          while (i < index) {
            i++;
            previous = current;
            current = current.next;
          }
          newNode.next = current;
          previous.next = newNode;
        }
        this.size++;
      }
    }
  
    removeFrom(index) {
      if (index < 0 || index >= this.size) {
        return null;
      } else {
        let current, previous, i = 0;
        current = this.head;
        previous = current;
  
        if (index === 0) {
          this.head = current.next;
        } else {
          while (i < index) {
            i++;
            previous = current;
            current = current.next;
          }
          previous.next = current.next;
        }
        this.size--;
        return current.element;
      }
    }
  
    removeElement(element) {
      let current = this.head;
      let previous = null;
  
      while (current !== null) {
        if (current.element === element) {
          if (previous === null) {
            this.head = current.next;
          } else {
            previous.next = current.next;
          }
          this.size--;
          return current.element;
        }
        previous = current;
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
      while (current) {
        str += current.element + " ";
        current = current.next;
      }
      console.log(str);
    }
  }
  