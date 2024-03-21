class Node:
    def __init__(self,value):
        self.value =value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =None
        self.tail = None

    def append(self,value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def preppend(self,value):
        newNode =Node(value)
        newNode.next = self.head
        self.head = newNode

        if not self.tail:
            self.tail = newNode

    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head= self.head.next
            if not self.head:
                self.tail = None
            return
        iterator = self.head
        while iterator.next:
            if iterator.next.value == value:
                iterator.next = iterator.next.next
                if not iterator.next:
                    self.tail = iterator
                return
            iterator = iterator.next

    def iterate(self):
        iterator = self.head
        while iterator :
            print(iterator.value+ " ")
            iterator = iterator.next