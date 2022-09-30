# 3 - Map Function
li = [1,2,3,4,5,6,7,8,9, 10]


def func(x):
    return x ** x

# map (function, list), do not call the function, 
# it will apply the function to every value of the list
print(list(map(func, li)))

# List comprehension
print([func(x) for x in li])