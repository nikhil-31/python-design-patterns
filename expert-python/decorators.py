
# This is the wrapper function, 
# it has a method inside it that will run something before 
# and after the passed in method.
def func(f):

    def wrapper(*args, **kwargs):
        print("Started")
        rv = f(*args, **kwargs)
        print("Ended")
        return rv
    
    return wrapper

def func2():
    print("I am function 2")

func2 = func(func2)
func2()

# Decorator, the above code can be shortned with
# a decorator
@func
def func3():
    print("i am function 3")

func3()


@func
def func4(x):
    print("i am function {}".format(x))

func4(4)

@func
def func4(x, y):
    print("i am function {}".format(x))
    return y
func4(5, 10)

import time

# Timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print("Time {}".format(str(total)))
        return rv
    return wrapper

@timer
def test():
    for _ in range(1000):
        pass

@timer
def test2():
    time.sleep(2)

test()
test2()