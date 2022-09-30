class Car: 
    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        """
        If no __str__ implementation is given. Python defaults to __repr__
        Should be unambiguous and used for developers
        """
        return '{}({},{})'.format(self.__class__.__name__, self.color, self.mileage)

my_car = Car('red', 2342)
print(repr(my_car))

# Containers will call the __repr__ function.
# Add a dunder repr to your classes
print(str([234,324,234]))