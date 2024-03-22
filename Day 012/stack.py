myStack = []

myStack.append(1)
myStack.append(2)
myStack.append(3)
myStack.append(4)
myStack.append(5)
myStack.append(6)

if len(myStack) > 0:
    poppedItem = myStack.pop()
    print("popped item {} from stack {}".format(poppedItem, myStack))