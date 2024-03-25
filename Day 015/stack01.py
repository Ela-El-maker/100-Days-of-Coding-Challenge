# creating a stack

def createStack():
    stack = []
    return stack

# creating an empty stack
def checkEmpty(stack):
    return len(stack) == 0


# Adding items into the stack

def push(stack,item):
    stack.append(item)
    print('Pushed Items : ' + item)

# Removing an element from the stack 

def pop(stack):
    if(checkEmpty(stack)):
        return 'Satck is empty'
    
    return stack.pop()


stack = createStack()

push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
push(stack, str(6))

print("Popped items : " + pop(stack))
print("Stack after popping an element : "+str(stack))