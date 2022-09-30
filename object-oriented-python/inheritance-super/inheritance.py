class Person:
    description = 'general person'

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def speak(self):
        print("My name is {} and i am {} years old.".format(self.name, self.age))

    def eat(self, food):
        print("{} eats {}.".format(self.name, food))

    def action(self):
        print("{} spins.".format(self.name))


class Baby(Person):
    # This will override `description` from the person class (Overriden attribute)
    description = 'baby'

    # Overriden method
    def speak(self):
        print("bha bah bha aks")

    def nap(self):
        print("{} takes a nap.".format(self.name))


person = Person('Steve', 20)
person.eat('roll')
person.speak()
person.action()

baby = Baby('zoot', 10)
baby.speak()
baby.eat('Baby food')
baby.action()

print(person.description)
print(baby.description)

print(isinstance(baby, object))

