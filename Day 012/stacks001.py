class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class Stack:
    def __init__(self):
        self.top =None

    def push(self, item):
        pass

    def pop(self):
        if not self.is_Empty():
            poppedItem = self.top.value
            self.top = self.top.next
            return poppedItem


    def is_Empty(self):
        return self.top is None
        