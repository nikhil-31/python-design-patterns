class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface
        return surface_area



class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def what_am_i(self):
        print('Rectangle')


# Square inherits from rectangle
class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)

    def what_am_i(self):
        print('Square')


class Cube(Square, SurfaceAreaMixin):

    def surface_area(self):
        face_area = self.area()
        return face_area * 6
    
    def volume(self):
        # Calling the super class method area 
        face_area = super().area()
        return face_area * self.length

    def what_am_i(self):
        print( 'Cube')


class Triangle:

    def __init__(self, base, height) -> None:
        self.height = height
        self.base = base
    
    def area(self):
        return 0.5 * self.base * self.height

    def what_am_i(self):
        print('Triangle')



class RightPyramid(Triangle, Square, SurfaceAreaMixin):
    def __init__(self, base, height, **kwargs) -> None:
        self.base = base
        self.slant_height = height


    def what_am_i(self):
        return 'RightPyramid'


cube = Cube(3)
print(cube.surface_area())
print(cube.perimeter())
super(Cube, cube).what_am_i()

square = Square(3)
print(square.area())
super(Square, square).what_am_i()

rectangle = Rectangle(3, 2)
print(rectangle.area())

# Multiple inheritance
right_pyramid = RightPyramid(2, 4)
# This will return the value from the first inherited parent (Triangle, Square)
super(RightPyramid, right_pyramid).what_am_i()
# Printing the bases 
print(right_pyramid.__class__.__bases__)

# MRO - Method resolution structure
# This is the order in which python will find methods and attributes
# Inheriting classes could have methods with the same name, use inheritance decleration order
# Directly access the class

print(RightPyramid.__mro__)