file = open("file.txt", "r")
try:
    file.write("lol")
finally:
    file.close()


# With keyword to use the context manager
with open("file.txt", "r") as file:
    file.write("Hello")

# A context manager with a generator
from contextlib import contextmanager

@contextmanager
def file(filename, method):
    print("enter")
    file = open(filename, method)
    yield file
    file.close()
    print("exit")

with file("text.txt", "w") as f:
    print("middle")
    f.write("hello")