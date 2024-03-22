class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self):
        self.front =None
        self.back = None
        self.size  =0

    def is_Empty(self):
        return self.size == 0

    def enqueue(self,value):
        newNode = Node(value)
        if self.is_Empty():
            self.front = self.back = newNode
        else:
            self.back.next = newNode
            self.back = newNode
        self.size += 1

    def dequeue(self,item):
        if not self.is_Empty():
            removedItem = self.front.value
            self.front = self.front.next
            self.size -= 1
            if self.is_Empty():
                self.back = None
                
            return removedItem
        else:
            print("Queue is empty")