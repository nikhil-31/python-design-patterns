# Lambda tutorial

def func(x):
    return x+5

print(func(2))

# Lamdba - Anonymous function
# to the left of the : is params, to the right is the function body and value that will be returned
# x( params): x + 5 (return value)
func2 = lambda x: x + 5
# Calling the lamdba function
print(func2(2))


func3 = lambda x, y=4: x + y
print(func3(3))

# Using with map and filter function
li = [1,2,3,4,5,6,7,8,9,10]


new_list = list(map(lambda x: x+5, li))
print(new_list)

new_list_2 = list(filter(lambda x: x % 2 == 0, li))
print(new_list_2)