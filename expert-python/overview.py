
# Method to make a class
def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name
        
        def print_value(self):
            print(x)
    return Dog

# Cls is the class itself, it's not an instance
cls = make_class(10)
d = cls('Nikhil')
d.print_value()

# For i in range 
for i in range(10):
    # Defining a function inside a for loop
    def show():
        print(i*2)
    show()

# Returning a function from a function
def func(x):
    if x == 1:
        def rv():
            print("x is equal to 1")
    else:
        def rv():
            print("x is not equal to 1")
    return rv

new_func = func(1)
new_func()

import inspect
from queue import Queue
print(id(new_func))
print(inspect.getsource(Queue))