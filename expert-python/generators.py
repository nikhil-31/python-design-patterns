
class Gen():

    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last ** 2
        self.last += 1
        return rv

# g = Gen(10000)

# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         print("Iteration stopped")
#         break
        
# Generator
def gen(n):
    for i in range(n):
        # Pauses the function here, until the function is 
        # called again
        yield i ** 2

g = gen(10000)

for i in g:
    print(i)




