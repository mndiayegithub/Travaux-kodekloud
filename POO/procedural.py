#Procedural Approach
# With the procedural approach, we separate data from the logic
# The data is stocked in the stack which is an empty list
stack = []

# The logic are the function push() and pop(), they can modify the value of the stack
def push(val): #Push value to stack
    stack.append(val)


def pop(): # Remove items and return them
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)
print(pop())
print(pop())
print(pop())

# The problem is that there's lot of disavantages
# The stack is vulnerable and anyone can modify it.