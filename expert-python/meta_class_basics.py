# Class will be passed into the test class
class Foo:
    def show(self):
        print("hi")

# Function will be sent as an attribute
def add_attribute(self):
    self.z = 9

Test = type('Test', (Foo,), {"x": 5, "add_attribute": add_attribute})
t = Test()

# Printing the class itself
print(Test)

# Printing an attribute passed into the class
print(t.x)

# We pass a class `Foo` when the test class is defined, 
# We are calling that classes method `Foo.show()`
t.show()

# We are calling a method that was passed to the class, the method will add an 
# attribute called `self.z` to the class and then we can print `z`
t.add_attribute()
print(t.z)

