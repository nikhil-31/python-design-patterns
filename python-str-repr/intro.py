class Car:
    
    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage

    def __str__(self) -> str:
        return 'a {} car'.format(self.color)

    def __repr__(self) -> str:
        pass

my_car = Car('red', 234324)
print(str(my_car))
print(my_car)