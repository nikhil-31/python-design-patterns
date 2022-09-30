# Filter function
def add_7(x):
    return x+7

def is_odd(x):
    if x % 2 != 0:
        return True 

li = [1,2,3,4,5,6,7,8,9,10]

# It will apply a function which gives a true or false value
b = list(filter(is_odd, li))
print(b)

c = list(map(add_7, filter(is_odd, li)))
print(c)