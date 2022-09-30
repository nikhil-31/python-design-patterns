class Person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This is a class method
    # you dont need to create an instance of a class to access this method
    # unlike, normal methods. To make a class method we should use 
    # @classmethod decorator, requires one parameter the class name itself
    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def is_adult(age):
        return age >= 18
    
    def display(self):
        print(self.name, ' is ', self.age, ' years old')


# Calling the class method, the class is not instantiated, 
# just using the class itself
print(Person.get_population())

# Calling static method
print(Person.is_adult(18))

new_person = Person('Tim', 18)

