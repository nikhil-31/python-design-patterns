from enum import Enum

class Animal(Enum):
    dog = 1
    cat = 2
    lion = 3

print(Animal.dog)

print(repr(Animal.dog))

print (type(Animal.dog))

print (Animal.dog.name)

for anim in Animal:
    print(anim)

print ("The enum member associated with value 2 is : ",end="")
print (Animal(2))