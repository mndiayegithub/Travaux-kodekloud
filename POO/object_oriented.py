#Object oriented
class Stack:
# Constructor - Create a new object each time this class is invoked
    def __init__(self):
        self.__stack_list= [] # Create a new stack list for each instance.
        # #__stack_list has been encapsulated and is only accessible in the class
        #print("I am in the constructor function ")

# Methods
        def push(self,val):
            self.__stack_list.append(val)

        def pop(self):
            val=self.__stack_list[-1]
            del self.__stack_list[-1]
            return val

# Subclass to do some maths
class AddingStack(Stack): # Create a class receiving a subclass as arguments
    def __init__(self):
        Stack.__init__(self) # Initialize the class.
        self.__sum=0 # Create the variable/data for the class and only accessible in the class.

    def get_sum(self):
        return self.__sum

    def push (self, val):
        self.__sum+=val
        Stack.push(self,val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum-=val


#stack_object = Stack()

#stack_object.push(3)
#stack_object.push(2)
#stack_object.push(1)

#print(stack_object.pop())
#print(stack_object.pop())
#print(stack_object.pop())

Stack = AddingStack()
Stack.push(3)
Stack.push(2)
Stack.push(1)
print(Stack.get_sum())

# Add more constructors to a class with an instance variable
# Adding constructors is like adding properties to a class.
class ExampleClass:
    def __init__(self, val = 1):
        self.first=val

    def second_set(self,val):
        self.second=val

# Not all objects have the same set of properties.
# To specify when an object contain a certain attribute, use hasttr function
# hasattr
# Specifies whether an instance contains a certain attribute


#print(len(stack_object.stack_list))