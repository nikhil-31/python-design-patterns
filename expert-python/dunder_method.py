class Person:
    def __init__(self, name):
        self.name = name
    
    # ToString method in java
    def __repr__(self):
        return f"Person({self.name})"
    
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid Argument, must be int")
        self.name = self.name * x

    def __call__(self, y):
        print("Called this function")

    def __len__(self):
        print(len(self.name))


person = Person('tim')
person(4)
print(person)
        