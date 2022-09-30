# Optional Parameter Tutorial


def func(x=5):
    return x ** 2

call = func(7)
print(call)

def func2(word, add=5, frequency=1):
    print(word*(frequency+5))


call2 = func2("Nikhil", 5, 5)

call3 = func2(2)