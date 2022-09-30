# Creating a meta class 

class Meta(type):

    def __new__(self, class_name, bases, attrs):
        # Called before the init method, its called first
        print(attrs)
        # Modifying the attrs
        a = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                a[key] = value
            else:
                a[key.upper()] = value
        print(a)
        return type(class_name, bases, a)

    def __init__():
        # Called after the new method
        pass


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")

d = Dog()
# We have changed the attr names to upper case, so x is now capital `X` 
# and `y` is `Y`, The function `hello` is `HELLO`
# print(d.x)
# print(d.hello())
print(d.HELLO())
print(d.X)